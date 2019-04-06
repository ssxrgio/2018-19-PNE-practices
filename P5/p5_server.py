import http.server
import socketserver
import termcolor

PORT = 8008

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET Received")
        print("Request line" + self.requestline)
        print("     Cnd:  " + self.command)
        print("Path:    " + self.path)

        termcolor.cprint(self.requestline, 'blue')
        if self.path == "/":
            with open("index.html", "r") as c:
                contents = c.read()
                c.close()
        elif self.path == "/blue.html":
            with open("blue.html", "r") as c:
                contents = c.read()
                c.close()
        elif self.path == "/pink.html":
            with open("pink.html", "r") as c:
                contents = c.read()
                c.close()
        elif self.path == "/green.html":
            with open("green.html", "r") as c:
                contents = c.read()
                c.close()
        else:
            with open("error.html", "r") as c:
                contents = c.read()
                c.close()

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        self.end_headers()

        self.wfile.write(str.encode(contents))

        return

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