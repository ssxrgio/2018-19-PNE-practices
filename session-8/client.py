import socket

# SERVER IP, PORT
IP = "212.128.253.106"
PORT = 8081

while True: # Instead of connecting the first time, just ask the user for the message so the server can attend other clients until the message is sent.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # The client is blocking the server....  NOT A GOOD DESIGN!!!
    msg = input("> ")

    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers respoinse
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()