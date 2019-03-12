import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8000

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'blue')

        # Open the form1.html file
        f = open("exform.html", 'r')
        contents = f.read()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the body of the response message
        self.wfile.write(str.encode(contents))

        return


''' SERVER MAIN PROGRAM '''

def find_msg(str):
    msg_pos = a.find('msg=') + 4
    letter_pos = a.find('&')
    input_msg = a[msg_pos:letter_pos]

    if '+' in input_msg:
        input_msg = input_msg.replace('+', ' ')

    return input_msg

# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

print("")
print("The Server is Stopped")