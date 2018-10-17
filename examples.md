# Examples

## networkmngr.py
```
pipenv run python networkmngr.py -p 4999 -a 6
6
Created a process
Created a process
Created a process
Created a process
Created a process
Created a process
About to get node
About to get node
About to get node
About to get node
About to get node
About to get node
All nodes downloaded
{'95436b1b9d3c4dba8b30cc8f47f4a571': '0.0.0.0:5000', '3d8ec94149a24415b4a7aeb84bf4002c': '0.0.0.0:5001', '1f240735e6be4ea7abc3659bf5ebca1f': '0.0.0.0:5002', '05bf5165b25846f79187326c875ce44d': '0.0.0.0:5003', '3edefed68ddf486aba261e74f85c0fae': '0.0.0.0:5004', 'ca6f7f411d774963b4428441e1f37f81': '0.0.0.0:5005'}
Nodes list sent to all nodes
 * Running on http://0.0.0.0:4999/ (Press CTRL+C to quit)
Sent mining request
Sent mining request
Sent mining request
Sent mining request
Sent mining request
Chain kept
Sent mining request
127.0.0.1 - - [17/Oct/2018 14:07:23] "GET /start/mining HTTP/1.1" 200 -
Chain kept
Chain kept
Chain kept
Chain kept
6
Miner shut
```
## eventblockchain.py
```
DEBUG:root:1539781572.1453161: Miner initiated, genesis block generated
DEBUG:root:1539781572.165057: Setting node indentificator to:
DEBUG:root:1539781572.165205: 95436b1b9d3c4dba8b30cc8f47f4a571
DEBUG:root:1539781572.1652951: Setting address
DEBUG:root:1539781572.165376: 0.0.0.0:5000
INFO:werkzeug: * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
DEBUG:root:1539781574.9662678: Getting node identificator
DEBUG:root:1539781574.9663832: Getting address
DEBUG:root:1539781574.9664419: Getting nodes list
DEBUG:root:{}
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:06:14] "GET /node/id HTTP/1.1" 200 -
DEBUG:root:1539781574.9913778: New nodes have been added
DEBUG:root:{'3d8ec94149a24415b4a7aeb84bf4002c': '0.0.0.0:5001', '1f240735e6be4ea7abc3659bf5ebca1f': '0.0.0.0:5002', '05bf5165b25846f79187326c875ce44d': '0.0.0.0:5003', '3edefed68ddf486aba261e74f85c0fae': '0.0.0.0:5004', 'ca6f7f411d774963b4428441e1f37f81': '0.0.0.0:5005'}
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:06:14] "POST /nodes/register HTTP/1.1" 201 -
DEBUG:urllib3.connectionpool:Starting new HTTP connection (1): 0.0.0.0:5001
DEBUG:urllib3.connectionpool:http://0.0.0.0:5001 "GET /chain HTTP/1.1" 200 223
DEBUG:root:1539781615.453238: Requested for node 0.0.0.0:5001's chain
DEBUG:root:1539781615.4533749: Chain received
DEBUG:urllib3.connectionpool:Starting new HTTP connection (1): 0.0.0.0:5002
DEBUG:urllib3.connectionpool:http://0.0.0.0:5002 "GET /chain HTTP/1.1" 200 223
DEBUG:root:1539781615.456936: Requested for node 0.0.0.0:5002's chain
DEBUG:root:1539781615.457063: Chain received
DEBUG:urllib3.connectionpool:Starting new HTTP connection (1): 0.0.0.0:5003
DEBUG:urllib3.connectionpool:http://0.0.0.0:5003 "GET /chain HTTP/1.1" 200 223
DEBUG:root:1539781615.460644: Requested for node 0.0.0.0:5003's chain
DEBUG:root:1539781615.460774: Chain received
DEBUG:urllib3.connectionpool:Starting new HTTP connection (1): 0.0.0.0:5004
DEBUG:urllib3.connectionpool:http://0.0.0.0:5004 "GET /chain HTTP/1.1" 200 223
DEBUG:root:1539781615.4644191: Requested for node 0.0.0.0:5004's chain
DEBUG:root:1539781615.464545: Chain received
DEBUG:urllib3.connectionpool:Starting new HTTP connection (1): 0.0.0.0:5005
DEBUG:urllib3.connectionpool:http://0.0.0.0:5005 "GET /chain HTTP/1.1" 200 223
DEBUG:root:1539781615.468155: Requested for node 0.0.0.0:5005's chain
DEBUG:root:1539781615.4683032: Chain received
DEBUG:root:1539781615.468362: Chain kept
DEBUG:root:1539781615.46843: Conflicts resolved
DEBUG:root:1539781615.5622919: Proof of mining: 41213
DEBUG:root:1539781615.562473: Block added to chain
DEBUG:root:1539781615.562537: 0.0.0.0:5001
DEBUG:root:1539781615.5647302: Broadcast sent to 0.0.0.0:5001 about new block
DEBUG:root:1539781615.5652149: 0.0.0.0:5002
DEBUG:root:1539781615.567692: Broadcast sent to 0.0.0.0:5002 about new block
DEBUG:root:1539781615.5681741: 0.0.0.0:5003
DEBUG:root:1539781615.571143: Broadcast sent to 0.0.0.0:5003 about new block
DEBUG:root:1539781615.571562: 0.0.0.0:5004
DEBUG:root:1539781615.5744169: Broadcast sent to 0.0.0.0:5004 about new block
DEBUG:root:1539781615.574938: 0.0.0.0:5005
DEBUG:root:1539781615.5869188: Broadcast sent to 0.0.0.0:5005 about new block
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:06:55] "GET /mine HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:06:57] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:06:58] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:06:58] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:06:58] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:06:58] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:06:58] "GET /chain HTTP/1.1" 200 -
DEBUG:root:1539781621.680018: Broadcast received of new block
DEBUG:root:1539781621.6803358: Getting address
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:01] "GET /block/new HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:02] "GET /chain HTTP/1.1" 200 -
DEBUG:root:1539781623.223294: Broadcast received of new block
DEBUG:root:1539781623.2235892: Getting address
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:03] "GET /block/new HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:03] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:05] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:05] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:05] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:05] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:06] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:06] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:06] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:06] "GET /chain HTTP/1.1" 200 -
DEBUG:root:1539781628.7114081: Chain replaced
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:08] "POST /chain/replace HTTP/1.1" 201 -
DEBUG:root:1539781628.732756: Chain replaced
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:08] "POST /chain/replace HTTP/1.1" 201 -
DEBUG:root:1539781629.1442392: Broadcast received of new block
DEBUG:root:1539781629.1444852: Getting address
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:09] "GET /block/new HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:10] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:11] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:11] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:11] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:11] "GET /chain HTTP/1.1" 200 -
DEBUG:root:1539781635.0590222: Chain replaced
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:15] "POST /chain/replace HTTP/1.1" 201 -
DEBUG:root:1539781635.4080389: Broadcast received of new block
DEBUG:root:1539781635.408282: Getting address
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:15] "GET /block/new HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:17] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:17] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:17] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:17] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:17] "GET /chain HTTP/1.1" 200 -
DEBUG:root:1539781642.351833: Chain replaced
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:22] "POST /chain/replace HTTP/1.1" 201 -
DEBUG:root:1539781642.716392: Broadcast received of new block
DEBUG:root:1539781642.716722: Getting address
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:22] "GET /block/new HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:24] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:24] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:24] "GET /chain HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:07:24] "GET /chain HTTP/1.1" 200 -
DEBUG:root:1539781682.6762502: Miner shut
INFO:werkzeug:127.0.0.1 - - [17/Oct/2018 14:08:02] "GET /shutdown HTTP/1.1" 200 -
DEBUG:root:1539781682.677689: App ended
```

More examples can be found in the /ExampleLogs folder