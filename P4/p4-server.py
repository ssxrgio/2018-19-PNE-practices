import socket
import termcolor

IP = "10.3.48.103"
PORT = 8090
MAX_OPEN_REQUESTS = 5


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    # Print the received message, for debugging
    print()
    print("Request message: ")
    termcolor.cprint(msg, 'blue')
    msglist = msg.split("\r\n")
    request = msglist[0]
    r = request.lstrip("GET").rstrip("HTTP/1.1")
    print(r)

    if r == " /pink ":
        with open("pink.html", "r") as c:
            contents = c.read()
            c.close()
    elif r == " /blue ":
        with open("blue.html", "r") as c:
            contents = c.read()
            c.close()
    elif r == " / ":
        with open("index.html", "r") as c:
            contents = c.read()
            c.close()
    else:
        with open("error.html", "r") as c:
            contents = c.read()
            c.close()

    # -- Everything is OK
    status_line = "HTTP/1.1 200 OK\r\n"

    # -- Build the header
    header = "Content-Type: text/html\r\n"
    header += "Content-Length: {}\r\n".format(len(str.encode(contents)))

    # -- Build the message by joining together all the parts
    response_msg = str.encode(status_line + header + "\r\n" + contents)
    cs.send(response_msg)

    # Close the socket
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)