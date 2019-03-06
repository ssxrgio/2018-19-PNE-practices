import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket created succesfully.\n')

port = 8081
IP = '212.128.253.105'

cond = True

while cond:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('\n---------------------------------\n  Socket created successfully.\n---------------------------------\n')
    s.connect((IP, port))


    sequence = input('Type a valid DNA sequence: ').upper()

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

