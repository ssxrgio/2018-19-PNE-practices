import http.server
import socketserver
import termcolor

PORT = 8075

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET Received")
        print("Request line" + self.requestline)
        print("     Cnd:  " + self.command)
        print("Path:    " + self.path)

        termcolor.cprint(self.requestline, 'blue')
        if self.path == "/":
            with open("ex1.html", "r") as c:
                contents = c.read()
        elif "msg" in self.path:
            with open("redirect_1.html", "r") as f:
                echo_mess = self.path[self.path.find("=")+1:]
                contents = f.read().format(echo_mess)
                f.close()
        else:
            with open("error.html", "r") as c:
                contents = c.read()
                c.close()

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        self.end_headers()

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