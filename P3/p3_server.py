import socket
from Seq import seq

PORT = 8081
IP = "192.168.1.49"
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

        msg = clientsocket.recv(2048).decode("utf-8")
        msg = msg.split(',')

        if not len(msg) == 2:
            message = '\nPlease, after the sequence, type a valid operation.'
            send_bytes = str.encode(str(message))

            clientsocket.send(send_bytes)
            clientsocket.close()

        else:
            print("Message from client: {}".format(msg))

            op = msg[1].strip(' ').lower()
            dna = seq(msg[0])

            dna_set = set('ACTG')

            if set(msg[0]).issubset(dna_set):

                if op == 'len':
                    message = '\nLenght of the sequence is {}.'.format(dna.len())
                    send_bytes = str.encode(str(message))

                    clientsocket.send(send_bytes)
                    clientsocket.close()

                elif op == 'complement':
                    message = '\nComplementary sequence is: {}.'.format(dna.complement())
                    send_bytes = str.encode(str(message))

                    clientsocket.send(send_bytes)
                    clientsocket.close()

                elif op == 'reverse':
                    message = '\nReverse sequence is: {}.'.format(dna.reverse())
                    send_bytes = str.encode(str(message))

                    clientsocket.send(send_bytes)
                    clientsocket.close()

                elif op == 'counta':
                    message = '\nNumber of \'As\' is: {}.'.format(dna.count('A'))
                    send_bytes = str.encode(str(message))

                    clientsocket.send(send_bytes)
                    clientsocket.close()

                elif op == 'countg':
                    message = '\nNumber of \'Gs\' is: {}.'.format(dna.count('G'))
                    send_bytes = str.encode(str(message))

                    clientsocket.send(send_bytes)
                    clientsocket.close()

                elif op == 'countc':
                    message = '\nNumber of \'Cs\' is: {}.'.format(dna.count('C'))
                    send_bytes = str.encode(str(message))

                    clientsocket.send(send_bytes)
                    clientsocket.close()

                elif op == 'countt':
                    message = '\nNumber of \'Ts\' is: {}.'.format(dna.count('T'))
                    send_bytes = str.encode(str(message))

                    clientsocket.send(send_bytes)
                    clientsocket.close()

                elif op == 'perca':
                    message = '\nPercentage of \'As\' is: {}%.'.format(dna.perc('A'))
                    send_bytes = str.encode(str(message))

                    clientsocket.send(send_bytes)
                    clientsocket.close()

                elif op == 'percg':
                    message = '\nPercentage of \'Gs\' is: {}%.'.format(dna.perc('G'))
                    send_bytes = str.encode(str(message))

                    clientsocket.send(send_bytes)
                    clientsocket.close()

                elif op == 'percc':
                    message = '\nPercentage of \'Cs\' is: {}%.'.format(dna.perc('C'))
                    send_bytes = str.encode(str(message))

                    clientsocket.send(send_bytes)
                    clientsocket.close()

                elif op == 'perct':
                    message = '\nPercentage of \'Ts\' is: {}%.'.format(dna.perc('T'))
                    send_bytes = str.encode(str(message))

                    clientsocket.send(send_bytes)
                    clientsocket.close()

                else:
                    message = '\nOperation not found/available.'
                    send_bytes = str.encode(str(message))

                    clientsocket.send(send_bytes)
                    clientsocket.close()
            
            else:
                message = '\nInvalid DNA sequence.'
                send_bytes = str.encode(str(message))

                clientsocket.send(send_bytes)
                clientsocket.close()

except socket.error:
    print("Problems using port {}.".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()