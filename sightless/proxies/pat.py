from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

class ProxyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            response = requests.get(self.path)
            self.send_response(response.status_code)
            self.send_header("Content-type", response.headers['Content-Type'])
            self.end_headers()
            self.wfile.write(response.content)
        except Exception as e:
            self.send_error(500, str(e))

def run(server_class=HTTPServer, handler_class=ProxyHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run(port=9999)
