import socket
import Crypto
from Crypto.PublicKey import RSA
#from crypto import Random
import ast
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Create a tuple server_address
server_address = ('localhost', 58432)
print 'Server: starting up on %s port %s' % server_address

# Bind the socket to the port
sock.bind(server_address)

# Listen for incoming connections - MAX 1 connection
sock.listen(1)

#RSA Settings
key = RSA.generate(1024) #generate pub and priv key

publickey = key.publickey() # pub key export for exchange
print('Server: publickey is %s' % key.exportKey())

while True:
    # Wait for a connection
    print 'Server: waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print 'Server: connection from', client_address

        #We send our public key
        print 'Server: sending publicKey to', client_address
        connection.send(key.exportKey())

        # Receive the data in small chunks and retransmit it
        while True:
            encryptedData = connection.recv(1024)
            print 'Server: received the encrypted message: "%s"' % encryptedData
            if encryptedData:
                print 'Server: is decrypting the message...'
                decrypted = key.decrypt(str(encryptedData))
                print'Server: decrypted data is: %s' % decrypted
            else:
                print 'Server: no more data from', client_address
                break

    finally:
        # Clean up the connection
        connection.close()