import socket
import sys

def server(port):        
    """Listen and receive a file, binding to the given port."""
    # Create a socket object specifying arguments to have UDP transport
    sock = socket.socket(PUT SOME ARGUMENTS HERE)

    # Bind the socket object to your localhost and port


    # Receive a filename and open a file
    data, address = sock.recvfrom(MAX_NUMBER_OF_BYTES)
    # Poll for all the data that should go into the file
    while "we don't get the control message":

    # Close the socket
    sock.close()

if __name__ == '__main__':
    if len (sys.argv) > 1:
        try:
            port = int(sys.argv[1])
            server (port)
        except ValueError:
            print ('Usage python3 server.py port\nport must be an int')
            sys.exit(0) 
    else:
            print ('Usage: python3 server.py port')
