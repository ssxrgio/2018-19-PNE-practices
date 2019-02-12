import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket created succesfully.\n')

port = 8080
IP = '212.128.253.64'

s.connect((IP, port))

while True:
    message = input('Type a message for the chat room: ')
    s.send(str.encode((message))) # For communicating we use bites, NOT STRINGS.

s.close()