import socket
from Seq import seq

PORT = 8081
IP = "192.168.0.162"
MAX_OPEN_REQUESTS = 5

number_con = 0

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serversocket.bind((IP, PORT))
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        number_con += 1

        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        lines1 = '-----------------------------------------------------------'
        lines2 = '-----------------------------------------------------------'
        mesg = 'Welcome to the Sequence Server. Please enter a valid sequence followed by one of the operations below:\n  · len: calculate the sequence length.\n  · complement: Calculate the complement.\n  · reverse: Calculate the reverse sequence.\n  · countBase : Calculate the number of a chosen base in the sequence. Note: if A wants to be counted, operation must be written like \'countA\'.\n  · percBase : Calculate the percentage of A bases in the sequence. Note: if percentage of As wants to be calculated, operation must be written like \'percA\'.'
        send_bytes = str.encode(str(mesg))
        send_lines = str.encode(str(lines1))
        send_lines2 = str.encode(str(lines2))

        clientsocket.send(send_lines)
        clientsocket.send(send_bytes)
        clientsocket.send(send_lines2)

        msg = clientsocket.recv(2048).decode("utf-8")

        msg = msg.split(',')
        print("Message from client: {}".format(msg))

        op = msg[1].strip(' ').lower()
        dna = seq(msg[0])

        if
        if op == 'len':
            message = '\nLenght of the sequence is {}'.format(dna.len())
            send_bytes = str.encode(str(message))

            clientsocket.send(send_bytes)
            clientsocket.close()

        elif op == 'complement':
            message = '\nComplementary sequence is: {}'.format(dna.complement())
            send_bytes = str.encode(str(message))

            clientsocket.send(send_bytes)
            clientsocket.close()

        elif op == 'reverse':
            message = '\nReverse sequence is: {}'.format(dna.reverse())
            send_bytes = str.encode(str(message))

            clientsocket.send(send_bytes)
            clientsocket.close()

        elif op == 'counta':
            message = '\nNumber of \'As\' is: {}'.format(dna.count('A'))
            send_bytes = str.encode(str(message))

            clientsocket.send(send_bytes)
            clientsocket.close()

        elif op == 'countg':
            message = '\nNumber of \'Gs\' is: {}'.format(dna.count('G'))
            send_bytes = str.encode(str(message))

            clientsocket.send(send_bytes)
            clientsocket.close()

        elif op == 'countc':
            message = '\nNumber of \'Cs\' is: {}'.format(dna.count('C'))
            send_bytes = str.encode(str(message))

            clientsocket.send(send_bytes)
            clientsocket.close()

        elif op == 'countt':
            message = '\nNumber of \'Ts\' is: {}'.format(dna.count('T'))
            send_bytes = str.encode(str(message))

            clientsocket.send(send_bytes)
            clientsocket.close()

        elif op == 'perca':
            message = '\nPercentage of \'As\' is: {}%'.format(dna.perc('A'))
            send_bytes = str.encode(str(message))

            clientsocket.send(send_bytes)
            clientsocket.close()

        elif op == 'percg':
            message = '\nPercentage of \'Gs\' is: {}%'.format(dna.perc('G'))
            send_bytes = str.encode(str(message))

            clientsocket.send(send_bytes)
            clientsocket.close()

        elif op == 'percc':
            message = '\nPercentage of \'Cs\' is: {}%'.format(dna.perc('C'))
            send_bytes = str.encode(str(message))

            clientsocket.send(send_bytes)
            clientsocket.close()

        elif op == 'perct':
            message = '\nPercentage of \'Ts\' is: {}%'.format(dna.perc('T'))
            send_bytes = str.encode(str(message))

            clientsocket.send(send_bytes)
            clientsocket.close()

        else:
            message = 'Operation not found/available. Try again.'
            send_bytes = str.encode(str(message))

            clientsocket.send(send_bytes)
            clientsocket.close()

except socket.error:
    print("Problems using port {}.".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()