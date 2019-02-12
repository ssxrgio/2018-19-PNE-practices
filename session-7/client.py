# Programming our first client.

import socket

# Create a socket for communicating with a server.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket created.\n')

port = 8080
IP = '212.128.253.64'

s.connect((IP, port))

while True:
    message = input('Type a message for the chat: ')
    s.send(str.encode((message))) # For communicating we use bites, NOT STRINGS.

s.close()

msg = s.recv(2048).decode('utf-8')

print('Message from the server: ',  msg)


print('The end')


