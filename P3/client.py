import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket created succesfully.')

port = 8081
IP = '192.168.0.162'

cond = True

while cond:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, port))

    lines = s.recv(2048).decode("utf-8")
    mesg = s.recv(2048).decode("utf-8")
    lines2 = s.recv(2048).decode('utf-8')

    print(lines)
    print(mesg)
    print(lines2)

    sequence = input('\nType a valid DNA sequence: ').upper()

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

