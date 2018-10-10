from argparse import ArgumentParser
import json
from flask import Flask, jsonify, request
import random
import requests
import hashlib
from time import time, sleep


class Conflict_resolver(object):
    def __init__(self, json_nodes, json_chain, initaddress):
        self.chain = json.loads(json_chain)
        self.nodes = json.loads(json_nodes)
        self.initaddress = initaddress
        self.resolve_conflicts()

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
            #print('Requested for node '+str(neighbours[node])+'\'s chain')

            #checks if the correct response received from the node
            if response.status_code == 200:
                #assigns values to variables from the response
                length = response.json()['length']
                chain=response.json()['chain']
                #print('Chain received')

                #checks if length is longer than min_length AND if the chain is valid
                #meaning the network is accepting the new chain and in turn new blocks on it.
                if length > min_length and self.valid_chain(chain):
                    #if true, sets new min_length and selects the longest out of all nodes chain, 
                    min_length = length
                    new_chain = chain

        #assigns the new longest chain replacing the current chain
        if new_chain:
            r = requests.post('http://'+initaddress+'/chain/replace', json = json.dumps(new_chain))
            #print("Chain replaced")
            return True
        print('Chain kept')
        return False

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

        #print('Chain valid')
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
    
    

# FLASK SECTION

# Instantiate our Node
#app = Flask(__name__)

# Instantiate a conflict resovler node
parser = ArgumentParser()
parser.add_argument('-n', '--json_nodes', default=None, type=str, help='json format of node\'s address')
parser.add_argument('-c', '--json_chain', default=None, type=str, help='chain')
parser.add_argument('-a', '--initaddress', default=None, type=str, help='address of initiaiting node')
args = parser.parse_args()
json_nodes = args.json_nodes
json_chain = args.json_chain
initaddress = args.initaddress
con = Conflict_resolver(json_nodes, json_chain, initaddress)
#app.run(host='0.0.0.0', port=random.randrange(4000, stop= 4998, step=1))
