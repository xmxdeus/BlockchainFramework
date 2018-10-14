# DecentralisedNetwork

Initially a learning experience, turned project, turned hobby.  
I decided I'll best understand blockchain technology by making my own.

Based on Satoshi Nakamoto’s Bitcoin: A Peer-to Peer Electronic Cash System.

Its a basic blockchain framework including:

+ Timeserver stamp
+ Proof of Work
+ HTTP requests
+ Consensus
+ Chain Validation

Using packages:

+ Flask 
+ Requests

This version DOES NOT run on multiple IP addresses but rather on multiple ports on your Macbook Pro.  
The framework comes with a set up manager tool called networkmngr.py. It's used to initialise a network of nodes, instruct to mine, setup a block or shut them down.

> _Later on I will implement IP nodes and convert from HTTP infrastructure to TCP ensuring less overhead and faster responses._

## Methodology

### Start up
Open Terminal. Go to the working directory this repository is stored in and run

'''bash
pipenv run python networkmngr.py -p 4999 -a 6
'''

### Background action
This will start the node manager client on localhost:4999 with 6 initial node clients (node ports start from 5000 and increment by 1). Firstly, they're started as processes in the background, next they intitialise themselves by:	
+ Genereting a random hash ID for itself
+ The manager downloads each node's ID and address 	
+ Manager compiles the list of all available nodes in the network and sends a copy to each so they're all _aware_ of each other
+ 

### NetworkMngr instructions

Send Mining requests to all nodes
> /start/mining 	
_Preset a specfic number of times to mine a block in network, in random 1-3s intervals_

Shutdown Network 
> /shutdown/all 	
_Stops all node clients_


### EventBlockchain instructions

Start Proof of Work for new block
> /block/new 
_On top of genesis or last block_

## To Do

+ Convert to TCP
+ Make Timestamp in Logs more readable
+ Add content in blocks
