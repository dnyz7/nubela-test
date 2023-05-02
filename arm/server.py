import socket
import sys
import os
import json

server_address = 'socks.sock'

# Make sure the socket does not already exist
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Bind the socket to the port
print('starting up on %s' % server_address)
sock.bind(server_address)

sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        #print('connection from', client_address)

        data = connection.recv(128)
        if data:
            print('received : "%s"' % data.decode('utf-8'))
            datadecode = data.decode('utf-8')
            storejson = datadecode.split('\n')
            #print('split : "%s"' % storejson)
            
            cleanjson = [i for i in storejson if i]
            #print('clean : "%s"' % cleanjson)

            pulljson = []
            listjson = {}
            finaljson = ''

            for idx, i in enumerate(cleanjson):
                #print('loop :',idx, i)
                convjson = json.loads(i)
                #print('convert :',convjson)
                xid = convjson['id']
                xfrom = convjson['from']
                xto = convjson['to']
                fiz = convjson['fizz']
                buz = convjson['buzz']
                
                for x in range(xfrom, xto+1):
                    if(x % 3 == 0 and x % 5 == 0):
                        # print(fiz+buz)
                        pulljson.append(fiz+buz)
                    elif(x % 3 == 0):
                        # print(fiz)
                        pulljson.append(fiz)
                    elif(x % 5 == 0):
                        # print(buz)
                        pulljson.append(buz)
                    else:
                        # print(x)
                        pulljson.append(x)

                #print('pulljson : ',pulljson)
                listjson[xid]=pulljson
                finaljson = finaljson + json.dumps(listjson) + '\n'
                pulljson = []
                listjson = {}
            
            
            print(finaljson)

        else:
                print ('no data from', client_address)
                break
            
    finally:
        # Clean up the connection
        connection.close()