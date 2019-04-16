import http.server
import socketserver
import termcolor
from Seq import Seq

PORT = 8008

def check_sequence(seq):
    bases = set("ACTG")

    if set(seq.upper()).issubset(bases):
        return True

    else:
        return False

    if len(seq) == 0:
        return False

    return True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        if "favicon.ico" in self.path:
            termcolor.cprint("\nPath: {}".format(self.path.replace("favicon.ico", "")), 'cyan')

        else:
            termcolor.cprint("\nPath: {}".format(self.path), 'cyan')

        if self.path == "/":

            with open("index.html", "r") as c:
                contents = c.read()
                c.close()

        elif "msg" in self.path:

            msg = self.path[self.path.find("=") + 1:self.path.find("&")] # This is the sequence written in the form
            termcolor.cprint("Sequence: {}".format(msg), 'yellow')

            if check_sequence(msg):
                with open("results.html", "r") as f:

                    seq = Seq(msg.upper())
                    base = self.path[self.path.find("base=") + 5]
                    operation = self.path[self.path.find("operation=") + 10:]

                    if operation == "perc":
                        operation = "Percentage"

                    elif operation == "count":
                        operation = "Count"

                    termcolor.cprint("Operation: {}".format(operation), 'blue')
                    termcolor.cprint("Base: {}".format(base), "blue")

                    if operation == "count":
                        op = seq.count(str(base))

                    else:
                        op = seq.perc(str(base))

                    if "chk" in self.path:
                        lenght = seq.len()
                        contents = f.read().format(msg.upper(), lenght, operation, base, op)

                    else:
                        contents = f.read().format(msg.upper(), "No selected", operation, base, op, )

                    f.close()

            else:
                with open("seq_error.html", "r") as c:
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