from argparse import ArgumentParser
import requests
import json

class Announcer(object):
    #this object will annouce to the 'port' of a new block
    def __init__(self, address):
        self.address = address
        r = requests.get('http://'+address+'/block/new')
        
parser = ArgumentParser()
parser.add_argument('-a', '--address', default=5000, type=str, help='port to listen on')
#parser.add_argument('-n', '--nodeSending', default=0, type=str, help='announcer\'s address')
#parser.add_argument('-c', '--chain', default=None, type=str, help='chain to be announced')
args = parser.parse_args()
#nodeSending = args.nodeSending
#chain = args.chain
address = args.address
Announcer(address)
