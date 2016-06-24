import socket
import Crypto
from Crypto.PublicKey import RSA
#from crypto import Random
import ast

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Create a tuple server_address
server_address = ('localhost', 58432)
print('Client: connecting to %s port %s' % server_address)

#connect to the server socket with TCP
sock.connect(server_address)

#RSA Settings
key = RSA.generate(1024) #generate pub and priv key

publickey = key.publickey() # pub key export for exchange
print('Client: publickey is %s' % key.exportKey())

encrypted = publickey.encrypt(int(input("Type your secret message here: ")), 32)

print('encrypted message:', encrypted) #ciphertext

decrypted = key.decrypt(ast.literal_eval(str(encrypted)))

#print('decrypted', decrypted)


try:
    # Send data
    message = 'This is the message.  It will be repeated.'
    print('Client: sending "%s"' % message)
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('Client: received "%s"' % data)

finally:
    print('Client: closing socket')
    sock.close()