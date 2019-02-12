# Programming our first client.

import socket

# Create a socket for communicating with a server.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket created.\n')

port = 8081
IP = '212.128.253.64'

s.connect((IP, port))

s.send(str.encode(('Hello world.'))) # For communicating we use bites, NOT STRINGS.

msg = s.recv(2048).decode('utf-8')

print('Message from the server: ',  msg)

s.close()

print('The end')


