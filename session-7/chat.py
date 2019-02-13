import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket created succesfully.\n')

port = 8080
IP = '192.168.0.160'

s.connect((IP, port))

cond = True

while cond:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created successfully.\n')
    s.connect((IP, port))

    message = input('Type a message for the chat room: ')

    if message == 'exit':
        print('\nYou have left the chat.')
        cond = False

    else:
        s.send(str.encode((message)))
        s.close()