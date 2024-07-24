from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('phi.html', 'rb') as file:  # Asegúrate de que el nombre del archivo HTML sea correcto
            self.wfile.write(file.read())

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        if ctype == 'multipart/form-data':
            fields = cgi.parse_multipart(self.rfile, pdict)
            data = fields.get('email')  # Asegúrate de que el nombre del campo coincida con el del formulario
            print("Datos recibidos:", data)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Recibido')

server = HTTPServer(('127.0.0.1', 8081), RequestHandler)
print("Servidor iniciado en http://127.0.0.1:8081")
server.serve_forever()
