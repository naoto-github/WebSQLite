from http.server import HTTPServer, CGIHTTPRequestHandler

class Handler(CGIHTTPRequestHandler):
    cgi_directories = ["/cgi-bin"]

PORT = 8080
HOST = "127.0.0.1"

httpd = HTTPServer((HOST, PORT), Handler)
httpd.serve_forever()
