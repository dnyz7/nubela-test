import socket
import sys
import os
import json

server_address = 'socks'

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
    print('waiting for a connection\n')
    connection, client_address = sock.accept()
    try:
        print('connection from client:', client_address)

        data = connection.recv(1024)
        if data:
            print('received data : \n"%s"' % data.decode('utf-8'))
            
            datadecode = data.decode('utf-8')
            storejson = datadecode.split('\n')
            print('split : "%s"' % storejson)
            
            cleanjson = [i for i in storejson if i]
            print('clean : "%s"' % cleanjson)

            pulljson = []
            listjson = {}
            finaljson = ''

            # for iter, i in enumerate(cleanjson):
            #     print('loop :',iter, i)
            #     convjson = json.loads(i)
                # print('convert :',convjson)
                # if "id" in convjson and "method" in convjson and "params" in convjson:
                #     id = convjson['id']
                #     method = convjson['method']
                #     if method == "echo":
                #         params = convjson['params']
                        
                #         listjson['id']=id
                #         listjson['result']=params
                #         finaljson = finaljson + json.dumps(listjson) + '\n'
                #     else:
                #         # print ('invalid message', client_address)
                #         print ('disconnected', client_address)
                #         connection.close()
                #         break
                    
                # else:
                #     # print ('invalid message', client_address)
                #     print ('disconnected', client_address)
                #     connection.close()
                #     break
            
            print('\n')
            print(finaljson)
            connection.sendall(finaljson)

        else:
                # print ('invalid message', client_address)
                print ('disconnected', client_address)
                connection.close()
                break
            
    finally:
        # Clean up the connection
        connection.close()