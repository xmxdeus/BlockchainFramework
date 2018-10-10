import hashlib
import json
from time import time
from flask import Flask, jsonify, request
import urllib3
import requests

# Each blockchain node can request for a new transaction to be calculated or
# be requested to mine a new transaction.

class Node(object):
    def __init__(self):        
        self.node_identificator = str()
        self.node_transactions = []
        self.nodes = {} #current nodes

    def register_node(self, node_identifier):
        """
        Add a new node to the list of nodes
        :param node_identifier: <str> identifier of node.
        :return: None
        """

        self.nodes[node_identifier] = []

class ArchivalNode(node):
    
        
class Miner(Node):
    def __init__(self):
        """
        Initialises the namespaces for an individual blockchain
        :param chain: <list> the blockchain
        """
        Node.__init__(self)
        self.chain = []
        self.orphan_chains = []
        # instead of transactions perhaps data for music.
        self.current_transactions = []
        
        #create genesis block
        self.new_block(previous_hash=1, proof=20)
        

    def new_block(self, previous_hash=None, proof):
        """
        Create new block in the blockchain
        :param proof: <int> proof from the Proof of Work algorithm
        :return: <dict> New Block
        """

        # Content of the block, the information that is due to be updated.
        # This should be updated in real time and only once the Work has been
        # completed and all validation done thats when data should be saved and
        # then updated from the chain if necessary.
        # This block saves the order it is at, when it happened ,and what is
        # to happen once the block has been mined and added to the blockchain,
        # such as calculating a value, or adding transactions, or removing users,
        # or runnning software that allows to distribute content within. And the
        # proof of work it needs, and the previous hash to create an integrated
        # blockchain.
        # Multiple types of blocks could also act an instruction set for another
        # node.
        
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transaction': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        
        
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        """

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
            

        return proof

    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid
        :param chain: <list> A blockchain
        :return: <bool> True if valid, False if not
        """
        # Should be realtime, deadline everytime the block is mined.
                
        last_block = chain[0] #genesis block
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(str(last_block))
            print(str(block))
            print("\n-----------\n")
            # Check that the hash of the block is correct
            if block['previous_hash'] != self.hash(last_block):
                return False

            # Check that the Proof of Work is correct
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False

            last_block = block
            current_index += 1

        return True
        
    def resolve_conflicts(self):
        """
        This is our Consensus Algorithm, it resolves conflicts
        by replacing our chain with the longest one in the network.
        :return: <bool> True if our chain was replaced, False if not
        """

        neighbours = self.nodes
        new_chain = None

        # We're only looking for chains longer than ours
        max_length = len(self.chain)

        # Grab and verify the chains from all the nodes in our network
        for node in neighbours:
            response = requests.get('http://'+ str(node) + '/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # Check if the length is longer and the chain is valid
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        # Replace our chain if we discovered a new, valid chain longer than ours
        if new_chain:
            self.orphan_chains.append(self.chain)
            self.chain = new_chain
            return True

        return False
    
    @property
    def last_block(self):
        # Returns the last Block in the chain
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """
        proof_string = str(last_proof) + str(proof)
        guess = proof_string.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:6] == "000000"

# FLASK SECTION

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate a Miner node
miner = Miner(node_identifier)

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    # Check that the required fields are in the POST'ed data
    required = ['sender', 'recipient', 'amount']
    #if not all(k in values for k in required):
 #      return 'Missing values', 400

    # Create a new Transaction
    index = miner.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': "Transaction will be added to Block " + str(index)}

    if len(self.chain) => 3:
        # We run the proof of work algorithm to get the next proof...
        last_block = miner.last_block
        last_proof = last_block['proof']
        proof = miner.proof_of_work(last_proof)

        # We must receive a reward for finding the proof.
        # The sender is "0" to signify that this node has mined a new coin.
        miner.new_transaction(
            sender="0",
            recipient=node_identifier,
            amount=1,
        )

        # Forge the new Block by adding it to the chain
        previous_hash = miner.hash(last_block)
        block = miner.new_block(proof, previous_hash)

        response = {
            'message': "New Block Forged",
            'index': block['index'],
            'transactions': block['transactions'],
            'proof': block['proof'],
            'previous_hash': block['previous_hash'],
            }
        
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': miner.chain,
        'length': len(miner.chain),
    }
    return jsonify(response), 200

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        miner.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(miner.nodes),
    }
    return jsonify(response), 201

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0', port=port)
