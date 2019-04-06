import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8026

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET Received")
        print("Request line" + self.requestline)
        print("     Cnd:  " + self.command)
        print("Path:    " + self.path)

        termcolor.cprint(self.requestline, 'blue')
        if self.path == "/":
            with open("ex2.html", "r") as c:
                contents = c.read()
        elif "msg" in self.path:
            if "chk" in self.path:
                mess = self.path
                mess1 = mess.split("&")
                capital = mess1[0].upper()
                with open("redirect_2.html", "r") as f:
                    echo_mess = capital[capital.find("=")+1:]
                    contents = f.read().format(echo_mess)
                    f.close()
            else:
                with open("redirect_2.html", "r") as f:
                    echo_mess = self.path[self.path.find("=")+1:]
                    contents = f.read().format(echo_mess)
                    f.close()
        else:
            with open("error.html", "r") as c:
                contents = c.read()
                c.close()




        # -- We want to generate a response message with the following command
        self.send_response(200)

        # --- Now we will define the content type and the header
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # We now finish the header
        self.end_headers()

        # We will now send the body of the response se message
        self.wfile.write(str.encode(contents))


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

print("")
print("Server Stopped")