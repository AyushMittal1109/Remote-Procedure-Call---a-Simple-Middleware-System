import socket
import json
from server_procedures import *
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('',12346))

s.listen(5)

while True:
	c,addr = s.accept()
	proto_str  = c.recv(1024).decode()
	proto_json = json.loads(proto_str)
	args = proto_json['values']
	del proto_json['values']
	proto_str = json.dumps(proto_json)

	if proto_str == '{"procedure_name": "foo", "parameters": [{"parameter_name": "par_1", "data_type": "int"}], "return_type": "str"}':
		ans = foo(args[0],)
		ans = str(ans)
		c.send(ans.encode())
		c.close()
		continue
	if proto_str == '{"procedure_name": "bar", "parameters": [{"parameter_name": "par_1", "data_type": "int"}, {"parameter_name": "par_2", "data_type": "str"}], "return_type": "int"}':
		ans = bar(args[0],args[1],)
		ans = str(ans)
		c.send(ans.encode())
		c.close()
		continue
