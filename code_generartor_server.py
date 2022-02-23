import json

fh = open('rpc_server.py','w')

f = open('contract.json','r')
contract = json.load(f)
f.close()

s = '''import socket
import json
from server_procedures import *
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('',12346))

s.listen(5)
'''

fh.write(s)

s = '''
while True:
\tc,addr = s.accept()
\tproto_str  = c.recv(1024).decode()
\tproto_json = json.loads(proto_str)
\targs = proto_json['values']
\tdel proto_json['values']
\tproto_str = json.dumps(proto_json)

'''

for fun in contract['remote_procedures']:
    proto_str = json.dumps(fun)
    s += "\tif proto_str == '"+proto_str + "':\n"
    s += "\t\tans = "+fun["procedure_name"]+"("
    args_count = len(fun["parameters"])
    for i in range(args_count):
        s+="args["+str(i)+"],"
    s+=")\n"

    s+="\t\tans = str(ans)\n"
    s+="\t\tc.send(ans.encode())\n"
    s+="\t\tc.close()\n"
    s+="\t\tcontinue\n"


fh.write(s)

fh.close()