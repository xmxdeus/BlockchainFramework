import hashlib
import json
from time import time, sleep
from flask import Flask, jsonify, request
import requests
from uuid import uuid4
import subprocess
import logging
import os #used to access cwd to store logs

class Miner(object):
    def __init__(self):
        """
        initialises the properties of this Miner, has id, list of nodes in network
        and the chain in the node
        """
        self.node_identificator = str()
        self._address = str()
        self.nodes = {}
        #chain inititated with genesis block already in place
        self.chain = [{
            'header': {
                'index': 1,
                'timestamp': time(),
                'proof': 20,
                'previous_hash': 1
                },
            'assembly instruction': None
            }]
        cwd = os.getcwd()
        LOG_FILE = cwd + '/Logs/' + str(time()) + self.node_identificator + '.log'
        logging.basicConfig(filename=LOG_FILE,level=logging.DEBUG)
        logging.debug(str(time()) + ': Miner initiated, genesis block generated')
        
    def register_node(self, node_identificator, address):
        """
        registers a node to the nodes set the miner has
        """
        self.nodes[node_identificator] = address
        if self.node_identificator == node_identificator:
            del self.nodes[node_identificator]

    def new_block(self, proof, previous_hash=None):
        """
        constructs a new block thats added into the chain
        """
        block = {
            'header': {
                'index': len(self.chain) + 1,
                'timestamp': time(),
                'proof': proof,
                'previous_hash': previous_hash or self.hash(last_block)
                },
            'assembly instruction': None #each block will have a section of code sent
            }

        self.chain.append(block)
        logging.debug(str(time()) + ': Block added to chain')
        #sends GET request broadcasting that a new block was mined to everyone
        #activating the resolve_conflicts on all nodes.
        
        for node in self.nodes:
            logging.debug(str(time()) + ': ' + str(self.nodes[node]))
            #needs to be run as a separate process
            process = subprocess.Popen(['python', '/Users/Amduz/Documents/blockchain/Announcer.py', '-a', self.nodes[node]])#, '-n', self.address, '-c', json.dumps(self.chain) #could implement a post request that will send block data to other nodes so that this node isnt bugged out.
            logging.debug(str(time()) + ': ' + 'Broadcast sent to '+str(self.nodes[node])+' about new block')

    @property
    def last_block(self):
        #getter that returns the last block in the chain
        return self.chain[-1]

    @property
    def node_identity(self):
        logging.debug(str(time()) + ': ' + 'Getting node identificator')
        
        return self.node_identificator

    @node_identity.setter
    def node_identity(self, node_ID):
        logging.debug(str(time()) + ': ' + 'Setting node indentificator to:')
        logging.debug(str(time()) + ': ' + node_ID)
        self.node_identificator = node_ID

    @property
    def address(self):
        logging.debug(str(time()) + ': ' + 'Getting address')
        return self._address

    @address.setter
    def address(self, address):
        logging.debug(str(time()) + ': ' + 'Setting address')
        logging.debug(str(time()) + ': ' + address)
        self._address = address

    @property
    def nodes_list(self):
        logging.debug(str(time()) + ': ' + 'Getting nodes list')
        logging.debug(self.nodes)
        return self.nodes

    def proof_of_work(self, last_proof):
        #this is where the mining happens
        """
        simple proof_of_work algorithm
        find new proof for the new block so that hash('lastproof''proof') has 6 leading zeros
        in the hash
        """
        proof = 0
        #this will check each proof number starting from 0 and iterate by 1 if its valid
        #in essence if it has 6 leading zeros.
        while self.valid_proof(last_proof, proof) is False:
            proof +=1
        logging.debug(str(time()) + ': ' + 'Proof of mining: '+str(proof))
        return proof

    def valid_chain(self, chain):
        """
        checks if the chain given is valid, are all the hashes correct
        """
        previous_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            if block['header']['previous_hash'] != self.hash(previous_block):
                return False
            if not self.valid_proof(previous_block['header']['proof'], block['header']['proof']):
                return False
            previous_block = block
            current_index += 1

        logging.debug(str(time()) + ': ' + 'Chain valid')
        return True

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        checks if last_proof and proof hashed together contain 6 leading zeros
        """
        #string of last_proof and proof put together
        proof_string = str(last_proof)+str(proof)
        guess = proof_string.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:5] == "00000"
        
    @staticmethod
    def hash(block):
        """
        creates a SHA-256 hash of a block (used for last blocks)
        """

        #block needs to be ordered for consistency, json.dumps() sorts the block
        #encode() then translates the object into json string format
        block_string = json.dumps(block, sort_keys=True).encode()
        #hashing using sha256 on the json string, returns a hash object then .hexdigest()
        #translates it into a string (hexbase hash)
        return hashlib.sha256(block_string).hexdigest()

    def resolve_conflicts(self):
        """
        this is the consensus algorithm that ensures to keep the longest chain
        itll be run when a block is broadcast right after its mined. all nodes run this.
        """
        neighbours = self.nodes
        new_chain = None

        #chains that are longer than the miniumum required length will result replacing this nodes chain
        min_length = len(self.chain)

        #for each node in the nodes list, request chains from their address!!!!
        for node in neighbours:
            response = requests.get('http://'+neighbours[node]+'/chain')
            logging.debug(str(time()) + ': ' + 'Requested for node '+str(neighbours[node])+'\'s chain')

            #checks if the correct response received from the node
            if response.status_code == 200:
                #assigns values to variables from the response
                length = response.json()['length']
                chain=response.json()['chain']
                logging.debug(str(time()) + ': ' + 'Chain received')

                #checks if length is longer than min_length AND if the chain is valid
                #meaning the network is accepting the new chain and in turn new blocks on it.
                if length > min_length and self.valid_chain(chain):
                    #if true, sets new min_length and selects the longest out of all nodes chain, 
                    min_length = length
                    new_chain = chain
                    logging.debug(str(time()) + ': ' + 'Chain longer?!')

        #assigns the new longest chain replacing the current chain
        if new_chain:
            self.chain = new_chain
            logging.debug(str(time()) + ': ' + "Chain replaced")
            return True
        logging.debug(str(time()) + ': ' + 'Chain kept')
        return False
    
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    logging.debug(str(time()) + ': ' + 'Miner shut')
    print('Miner shut')

    
# FLASK SECTION

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identity = str(uuid4()).replace('-', '')

# Instantiate a Miner node
miner = Miner()



@app.route('/block/new', methods=['GET'])
def notified_new_block():
    logging.debug(str(time()) + ': ' + 'Broadcast received of new block')
    #opens a new flask server that will resolve the conflict for this particular node and then save its chain
    process = subprocess.Popen(['pipenv', 'run', 'python', '/Users/Amduz/Documents/blockchain/ResolveConflicts.py', '-n', json.dumps(miner.nodes), '-c', json.dumps(miner.chain), '-a', miner.address])#
    
    response = 'Notified'
    return jsonify(response), 200

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': miner.chain,
        'length': len(miner.chain)
    }
    return jsonify(response), 200

@app.route('/chain/replace', methods=['POST'])
def replace_chain():
    json_chain=request.get_json()
    miner.chain = json.loads(json_chain)
    response ='Chain replaced'
    logging.debug(str(time()) + ': ' + response)
    return jsonify(response), 201

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    json_values = request.get_json()
    values = json.loads(json_values)
    nodes = values.get('nodes')
    addresses = values.get('addresses')
    
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node, address in zip(nodes, addresses):
        miner.register_node(node, address)
    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(miner.nodes),
    }
    logging.debug(str(time()) + ': ' + response['message']) #algorithm of finding needs to be worked on
    logging.debug(miner.nodes)
    return jsonify(response), 201

@app.route('/mine', methods=['GET'])
def mine():
    #need to make the process separate as an interrupt is required for new block event
    miner.resolve_conflicts()
    logging.debug(str(time()) + ': ' + 'Conflicts resolved')
    # We run the proof of work algorithm to get the next proof...
    last_block = miner.last_block
    last_proof = last_block['header']['proof']
    proof = miner.proof_of_work(last_proof)

    # We must receive a reward for finding the proof.
    # The sender is "0" to signify that this node has mined a new coin.
##    miner.new_transaction(
##        sender="Blockchain",
##        recipient=node_identity,
##        amount=40,
##    )

    # Forge the new Block by adding it to the chain
    previous_hash = miner.hash(last_block)
    block = miner.new_block(proof, previous_hash)
    response = 'Mined'
    
    return jsonify(response), 200

@app.route('/node/id', methods=['GET'])
def get_node_id():
    response = {
        'node': miner.node_identity,
        'address': miner.address,
        'nodes': miner.nodes_list
        }
    return jsonify(response), 200

@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return jsonify('Server shutting down...'), 200 

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    miner.node_identity = node_identity
    miner.address = '0.0.0.0:'+str(port)
    app.run(host='0.0.0.0', port=port)
    logging.debug(str(time()) + ': ' + 'App ended')
    
