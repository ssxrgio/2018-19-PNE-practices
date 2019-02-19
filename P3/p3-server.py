import socket
from Seq import seq

# Configure the Server's IP and PORT
PORT = 8081
IP = "212.128.253.106"
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Another connection!
        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any
        msg = clientsocket.recv(2048).decode("utf-8")
        print('\nMessage {}'.format(msg))

        if msg == ' ':
            response = '-----------------------------\n   Server currently alive.\n-----------------------------\n '
            send_response = str.encode(response)
            clientsocket.send(send_response)
            clientsocket.close()

        else:
            response = 'len: calculate the sequence length.\ncomplement: Calculate the complement.\nreverse: Calculate the reverse sequence.\ncountBase: Calculate the number of a base (A, C, T, G) in the sequence.\npercBase: Calculate the percentage of a base (A, C, T, G) in the sequence.\n'
            send_response = str.encode(response)
            clientsocket.send(send_response)
            clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()