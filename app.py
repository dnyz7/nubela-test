import socket
import sys
import os
import json

#server_address = '/Users/dennyhusniansyah/development/py/landx-test/socks.sock'

if len(sys.argv)>1:
    server_address = sys.argv[1]

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
                print('split : "%s"' % storejson)
                
                # cleanjson = [i for i in storejson if i]
                #print('clean : "%s"' % cleanjson)

                pulljson = []
                listjson = {}
                finaljson = '{"id": 42, "result": {"message": "Hello"}}'

                # for idx, i in enumerate(cleanjson):
                #     #print('loop :',idx, i)
                #     convjson = json.loads(i)
                #     #print('convert :',convjson)
                #     xid = convjson['id']
                    

                #     #print('pulljson : ',pulljson)
                #     listjson[xid]=pulljson
                #     finaljson = finaljson + json.dumps(listjson) + '\n'
                #     pulljson = []
                #     listjson = {}
                
                
                # print(finaljson)
                connection.sendall(finaljson.encode('utf-8'))
            else:
                    print ('no data from', client_address)
                    break
                
        finally:
            # Clean up the connection
            connection.close()
else:
    print ('no path sock file')
    
