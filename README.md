# BlockchainFramework

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

### Useful Tools

+ Postman.app (you can use your browser to enter localhost requests)

## Methodology

### Prerequisites

Open Terminal. Go to the working directory this repository is stored in. Before starting the program, optionally, run the below command to remove unecessary 'Courtesy Notices' being displayed. Or add it to your _.bash_profile_ file.

```export PIPENV_IGNORE_VIRTUALENVS=0```

### Start up

To create your network of nodes execute:

```pipenv run python networkmngr.py -p 4999 -a 6```

#### Background action

This will start the node manager client on localhost:4999 with 6 initial node clients (node ports start from 5000 and increment by 1). Firstly, they're started as processes in the background, next they are initialised by:	
+ Genereting a random hash ID for itself
+ The manager downloads each node's ID and address 	
+ Manager compiles the list of all available nodes in the network and sends a copy to each so they're all _aware_ of each other
+ 

### NetworkMngr instructions

+ Send Mining requests to all nodes

_[address]:[port]/start/mining_

> Preset to a specfic number of times to mine a block in network, in random 1-3s intervals

+ Shutdown Network 

_[address]:[port]/shutdown/all_

> Stops all node clients


### EventBlockchain instructions

+ Notify node of new block being successfully mined

_[address]:[port]/block/new_

> The node will run ResolveConflicts.py to update it's chain based on the established Consensus

+ Get chain

_[address]:[port]/chain_

> Returns the current chain

+ Replace chain

_[address]:[port]/chain/replace_

> Will replace node's chain w/ the one provided in this POST request (json format only)

+ Register nodes list

_[address]:[port]/nodes/register_

> Adds listed supplied json list of nodes to the node's registry

+ Mine

_[address]:[port]/mine_

> One last time run ResolveConflicts.py before Node starts proof of work on HEAD block's hash (current master chain)

+ Get Node Status

_[address]:[port]/node/id_

> Returns the node's ID, address and their known record of other nodes (should make it a limit and give group bands of IP addresses eg. 100.0.3.xxx = 255 group members)

+ Shutdown Node

_[address]:[port]/shutdown_

> Shuts the node down and sends response (need more secure and checks)

## Examples 

Can be found inside examples.md file. It shows how the two networkmngr.py instructins function. _(need to add timestamps for networkmngr.py)_

## To Do

+ Convert to TCP
+ Make Timestamp in Logs more readable
+ Add content in blocks
+ Implement a check to see if childprocesses terminated before shutting Manager.
+ Node ID, addresses and etc need to be put into files.
+ Create Flowchart
+ Add error handling
+ Change order of mining response in networkmngr.py