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

#We receive the key
data = sock.recv(2048)

#RSA Settings
key = RSA.importKey(data)
publickey = key.publickey() # pub key export for exchange

print('Client: the server publickey is %s' % key.exportKey())
try:
    # Send data
    message = input('Please type the message you want to send to the server: ')
    print('Client: message is "%s"' % message)

    #Encryption
    encrypted = publickey.encrypt(message)
    print('Client: will send the following encrypted message "%s"' % encrypted)

    sock.sendall(encrypted)
finally:
    print('Client: closing socket')
    sock.close()