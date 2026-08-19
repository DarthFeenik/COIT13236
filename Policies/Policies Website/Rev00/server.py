import http.server
import socketserver
import os
from urllib.parse import urlparse, parse_qs

PORT = 8000
POLICY_FOLDER = "policies-folder"
READ_FILE = "filereads.csv"

class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        # Endpoint: /list
        if self.path == "/list":
            try:
                files = os.listdir(POLICY_FOLDER)
                allowed = [f for f in files if f.lower().endswith((".doc", ".docx", ".pdf"))]
                response = "\n".join(allowed)
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(response.encode())
            except Exception as e:
                self.send_error(500, str(e))
            return

        # Default: serve files normally
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        # Endpoint: /record_read
        if self.path == "/record_read":
            length = int(self.headers["Content-Length"])
            data = self.rfile.read(length).decode()

            with open(READ_FILE, "a") as f:
                f.write(data)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
            return

        self.send_error(404, "Unknown POST endpoint")


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    httpd.serve_forever()
