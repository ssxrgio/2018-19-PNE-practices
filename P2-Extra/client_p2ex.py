import socket

port = 8080
IP = '192.168.56.1'

cond = True

while cond:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created successfully.\n')
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
        print("Complementary sequence: {}".format(msg))
        s.close()

