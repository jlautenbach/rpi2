import BaseHTTPServer

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        message = self.rfile.read(length).decode()
        print(f'Received message from client: {message}')

server = BaseHTTPServer.HTTPServer(('', 8000), RequestHandler)
server.serve_forever()
