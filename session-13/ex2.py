import http.server
import socketserver
import termcolor

PORT = 8009

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

        filename = "index.html"

        with open(filename) as f:
            contents = f.read()
            f.close()

        self.send_response(200)

        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(str.encode(contents)))

        self.end_headers()

        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------

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