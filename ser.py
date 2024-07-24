from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        if ctype == 'multipart/form-data':
            fields = cgi.parse_multipart(self.rfile, pdict)
            data = fields.get('nombre_del_campo')
            print("Datos recibidos:", data)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Recibido')

server = HTTPServer(('127.0.0.1', 8081), RequestHandler)
print("Servidor iniciado en http://127.0.0.1:8081")
server.serve_forever()
