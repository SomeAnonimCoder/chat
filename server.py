from http.server import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep

ROOT = curdir + sep + "client"


class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"

        try:
            # Check the file extension required and
            # set the right mime type
            sendReply = False

            if self.path.endswith(".html"):
                mimetype = 'text/html'
                sendReply = True
            elif self.path.endswith(".jpg"):
                mimetype = 'image/jpeg'
                sendReply = True
            elif self.path.endswith(".gif"):
                mimetype = 'image/gif'
                sendReply = True
            elif self.path.endswith(".js"):
                mimetype = 'application/javascript'
                sendReply = True
            elif self.path.endswith(".css"):
                mimetype = 'text/css'
                sendReply = True


            if sendReply == True:
                # Open the static file requested and send it
                f = open(ROOT + sep + self.path, "rb")
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()


            return



        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)




def run():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ("0.0.0.0", 8080)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


run()