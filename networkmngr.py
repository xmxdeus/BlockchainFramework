#before registering, this code will download all node id and address associated.
#registers all nodes to all nodes, depending on how many were created.
import hashlib
import json
import time
from flask import Flask, jsonify, request
import requests
from uuid import uuid4
import subprocess
import random


def start(amount):
    processes = {}
    print(amount)
    for i in range(amount):
        #Starts each node in the background.
        pargz = ['pipenv', 'run', 'python', 'eventblockchain.py', '-p', str(5000+i)]
        subprocess.Popen(pargz)
        print('Created a process')
    #delay to let the miners wake up to full operating mode.
    time.sleep(5)
    node.download_node_info(amount)
    node.register_to_all(amount)
    mine_requests = 10000

class Boss_node(object):
    def __init__(self):
        self.nodes = {}

    def download_node_info(self, amount):
        for i in range(amount):
            print('About to get node')
            node_info = requests.get('http://0.0.0.0:'+str(i+5000)+'/node/id')
            self.nodes[node_info.json()['node']] = node_info.json()['address']
        print('All nodes downloaded')
        print(self.nodes)
        
    def register_to_all(self, amount):
        for i in range(amount):
            r = requests.post('http://0.0.0.0:'+str(i+5000)+'/nodes/register', json = json.dumps(self.format_to_register(self.nodes)))
        print('Nodes list sent to all nodes')

    @staticmethod
    def format_to_register(nodes):
        form = {}
        form['nodes'] = []
        form['addresses'] = []
        for node in nodes:
            form['nodes'].append(node)
            form['addresses'].append(nodes[node])
        return form

    def send_to_mine(self, address):
        v = requests.get('http://'+str(address)+'/mine')

    def begin_sending(self, amount):
##        with open('important_script.rtf', 'r') as f:
##            read_data = f.read()
##        for word in read_data:
    #add command that adds a single word to the block
            for n in range(amount):
                self.send_to_mine('0.0.0.0:'+str(5000+n))
                print('Sent mining request')
                time.sleep(random.randrange(1, stop=3, step=1))

def shutdown_server():
    print(amount)
    for i in range(amount):
        node_info = requests.get('http://0.0.0.0:'+str(i+5000)+'/shutdown')
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    print('Manager shut')
    

# FLASK SECTION

# Instantiate our Node
app = Flask(__name__)

# Instantiate a boss node
node = Boss_node()

@app.route('/shutdown/all', methods=['GET'])
def shutdown():
    shutdown_server()
    return jsonify('Servers will be shut down...'), 200

@app.route('/start/mining', methods=['GET'])
def mining():
    for n in range(1):
        node.begin_sending(amount)
    return jsonify('Beggining mining'), 200

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5010, type=int, help='port to listen on')
    parser.add_argument('-a', '--amount', default=5010, type=int, help='amount of servers to run')
    args = parser.parse_args()
    port = args.port
    amount = args.amount
    start = start(amount)
    app.run(host='0.0.0.0', port=port)

