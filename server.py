import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Create a tuple server_address
server_address = ('localhost', 58432)
print 'Server: starting up on %s port %s' % server_address

# Bind the socket to the port
sock.bind(server_address)

# Listen for incoming connections - MAX 1 connection
sock.listen(1)

while True:
    # Wait for a connection
    print 'Server: waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print 'Server: connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print 'Server: received "%s"' % data
            if data:
                print 'Server: sending data back to the client'
                connection.sendall(data)
            else:
                print 'Server: no more data from', client_address
                break

    finally:
        # Clean up the connection
        connection.close()