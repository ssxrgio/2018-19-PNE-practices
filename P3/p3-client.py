import socket

port = 8081
IP = '212.128.253.106'

cond = True

while cond:
    sequence = input('Type a valid DNA sequence: ').upper()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('\n---------------------------------\n  Socket created successfully.\n---------------------------------\n')
    s.connect((IP, port))

    if sequence == 'EXIT':
        print('\n-----------------------')
        print('      Exit server.')
        print('-----------------------')
        cond = False

    else:
        s.send(str.encode(sequence))
        msg = s.recv(2048).decode("utf-8")
        print(msg)
        s.close()

    if msg[0:3] == 'len':
        sequence = input('Choose a valid option from above: ').upper()