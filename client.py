import socket
import sys

if len(sys.argv)>1:
    server_address = sys.argv[1]

    # Create a UDS socket
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    
    # Connect the socket to the port where the server is listening
    # server_address = '/Users/dennyhusniansyah/dev/nubela/landx-test/socks.sock'
    print('connecting to %s' % server_address)
    try:
        sock.connect(server_address)
    except socket.error as msg:
        print('Socket Error: %s' % msg)
        sys.exit(1)
    try:
        
        # Send data
        # message = '{"id":"one","from":0,"to":15,"fizz":"zzif","buzz":"zzub"}\n{"id":"two","from":6,"to":10,"fizz":"zzif2","buzz":"zzub2"}\n'
        message = '{"id":1,"method":"echo","params": {"message": "Hello"}}\n{"id":2,"method":"echo","params": {"message": "Good morning"}}'
        print('sending "%s"' % message)
        sock.sendall(message.encode('utf-8'))

    finally:
        print('closing socket')
        sock.close()
else:
    print ('no path sock file')