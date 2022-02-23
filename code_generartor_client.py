import json

fh = open('rpc_client.py','w')

s = '''import socket
import json

port = 12346

f = open("contract.json")
data = json.load(f)
f.close()
'''

fh.write(s)

f = open('contract.json','r')
contract = json.load(f)
f.close()

# print(contract,type(contract))

for fun in contract['remote_procedures']:
    # print(fun)
    protocol = str(fun)
    fun_name = fun['procedure_name']
    para_count = len(fun['parameters'])
    fun_def = 'def ' + fun_name + '('
    for i in range(para_count):
        fun_def+='a'+str(i)+','
    fun_def+='): \n'

    fh.write(fun_def)

    ## list of all arguments
    S = "\targs = ["
    for i in range(para_count):
        S+= "a"+str(i)+','
    S+=']\n'
    fh.write(S)

    ## appending values in protocol
    fh.write("\tprotocol = "+protocol+"\n")
    S = '\tprotocol["values"] = args\n'
    S+="\tprotocol = json.dumps(protocol)\n"
    # S+="\tprotocol = '\"' + protocol + '\"'\n"
    # S+="\tprint(protocol)\n"
    S+='''\ts = socket.socket()\n\ts.connect(('127.0.0.1', port))\n\ts.send(protocol.encode())\n\treply = s.recv(1024).decode()\n'''
    fh.write(S)

    ##type casting properly
    # if fun['return_type']=='string':
    #     fun['return_type'] = 'str'
    S = "\treply = "+fun['return_type']+'(reply)\n\treturn reply\n\n'
    fh.write(S)


fh.close()