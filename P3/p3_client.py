import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket created succesfully.')

port = 8081
IP = '192.168.1.49'

cond = True

while cond:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, port))

    sequence = input('\nPlease, type a valid DNA sequence followed by an operation by a \',\': ').upper()

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

