from http.server import HTTPServer, CGIHTTPRequestHandler

class Handler(CGIHTTPRequestHandler):
    # CGIを設置するディレクトリ
    cgi_directories = ["/cgi-bin"]

# ポート番号
PORT = 8080

# IPアドレス
HOST = "127.0.0.1"

print("http://localhost:8080/cgi-bin/sql.py")
print("http://localhost:8080/cgi-bin/sql.py?id=A001")

# サーバの起動
httpd = HTTPServer((HOST, PORT), Handler)
httpd.serve_forever()

