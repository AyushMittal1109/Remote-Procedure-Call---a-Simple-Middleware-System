# Remote Procedure Call - a Simple Middleware System
This allows dynamically adding a service into the system and allows accessing the service from a client program. A RPC protocol consisting of Server Stub and Client Stub, responsible to run any given function present in server machine as shared library on client side. Communication protocol used is socket.
***
## A Simple walk through:
#### Following files are initially available : 
* `Client.py`
* `server_precodeures.py`
* `contract.json`

#### Following files are made as part of Remote procedure call implementation :
* `code_generartor_client.py` - this will generate `rpc_client.py` based on contract provided. `rpc_client.py` contains client-side stub for every procedure defined in `rpc_server.py`.
* `code_generartor_server.py` - this will generate `rpc_server.py` based on contract provided. `rpc_server.py` contains server-side stub for every procedure defined in `rpc_server.py`, also generic listener which will listen the client stub request and function caller to call procedure residing in `server_precodeures.py`.


## Working
* run `code_generator_client.py` using following command `python code_generator_client.py contract.json`, This will generate the `rpc_client.py` which will have client side stubs for every procedures defined in `contract.json`.
*  run `code_generator_server.py` using following command `python code_generator_server.py contract.json`, This will generate the `rpc_server.py` which will have server side stubs for every procedures defined in `contract.json`. 
*  `python rpc_server.py`
*  `python client.py`

***
## Assumptions
* All files will be put in same directory
* All files should be generated in same directory
* `client.py` will include `rpc_client.py`.
* `server.py` contains only procedure and its implementation which you will include 