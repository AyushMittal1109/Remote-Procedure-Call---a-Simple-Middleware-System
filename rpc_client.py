import socket
import json

port = 12346

f = open("contract.json")
data = json.load(f)
f.close()
def foo(a0,): 
	args = [a0,]
	protocol = {'procedure_name': 'foo', 'parameters': [{'parameter_name': 'par_1', 'data_type': 'int'}], 'return_type': 'str'}
	protocol["values"] = args
	protocol = json.dumps(protocol)
	s = socket.socket()
	s.connect(('127.0.0.1', port))
	s.send(protocol.encode())
	reply = s.recv(1024).decode()
	reply = str(reply)
	return reply

def bar(a0,a1,): 
	args = [a0,a1,]
	protocol = {'procedure_name': 'bar', 'parameters': [{'parameter_name': 'par_1', 'data_type': 'int'}, {'parameter_name': 'par_2', 'data_type': 'str'}], 'return_type': 'int'}
	protocol["values"] = args
	protocol = json.dumps(protocol)
	s = socket.socket()
	s.connect(('127.0.0.1', port))
	s.send(protocol.encode())
	reply = s.recv(1024).decode()
	reply = int(reply)
	return reply

