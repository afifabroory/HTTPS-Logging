from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
import ssl

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        print(self.client_address)
        print(self.path)
        print(self.headers)
        print(self.rfile.read())


server_address = ('0.0.0.0', 443)
httpd = HTTPServer(server_address, HTTPRequestHandler)
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain('cert.pem', 'key.pem')
httpd.socket = ctx.wrap_socket(httpd.socket, True)
httpd.serve_forever()