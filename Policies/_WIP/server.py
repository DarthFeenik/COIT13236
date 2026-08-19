import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

PORT = 8000

# Get absolute path of the folder where server.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

POLICY_FOLDER = os.path.join(BASE_DIR, "policies-folder")
READ_FILE = os.path.join(BASE_DIR, "filereads.csv")
RENEWAL_FILE = os.path.join(BASE_DIR, "policyrenewal.csv")
ACCOUNTS_FILE = os.path.join(BASE_DIR, "accounts.csv")

# Automatically create the policies-folder if it somehow disappeared
if not os.path.exists(POLICY_FOLDER):
    os.makedirs(POLICY_FOLDER)

class Handler(BaseHTTPRequestHandler):

    def send_text(self, text):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        # Added CORS headers to prevent modern browsers from blocking the response data
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.end_headers()
        self.wfile.write(text.encode())

    def send_file(self, path):
        if not os.path.exists(path):
            self.send_error(404, "File not found")
            return

        with open(path, "rb") as f:
            data = f.read()

        self.send_response(200)
        # Handle correct content types so browsers don't download them as raw text
        if path.endswith(".html"):
            self.send_header("Content-Type", "text/html")
        elif path.endswith(".csv"):
            self.send_header("Content-Type", "text/csv")
        else:
            self.send_header("Content-Type", "application/octet-stream")
            
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        parsed = urlparse(self.path)

        # Serve HTML files
        if self.path.endswith(".html"):
            return self.send_file(os.path.join(BASE_DIR, self.path[1:]))

        # Serve CSV files
        if self.path.endswith(".csv"):
            return self.send_file(os.path.join(BASE_DIR, self.path[1:]))

        # /list → list policy files
        if parsed.path == "/list":
            try:
                allowed = []
                # Ensure the folder exists before reading
                if os.path.exists(POLICY_FOLDER):
                    for item in os.listdir(POLICY_FOLDER):
                        item_path = os.path.join(POLICY_FOLDER, item)
                        # Check strictly for target extensions
                        if os.path.isfile(item_path) and item.lower().endswith((".doc", ".docx", ".pdf")):
                            allowed.append(item)
                
                # Send the plain text list back to the browser interface
                return self.send_text("\n".join(allowed))
            except Exception as e:
                self.send_error(500, str(e))
                return

        # /reads → return filereads.csv
        if parsed.path == "/reads":
            if not os.path.exists(READ_FILE):
                return self.send_text("FileName,Account,DateRead\n")
            with open(READ_FILE, "r") as f:
                return self.send_text(f.read())

        # /renewal → return policyrenewal.csv
        if parsed.path == "/renewal":
            if not os.path.exists(RENEWAL_FILE):
                return self.send_text("FileName,HoursValid\n")
            with open(RENEWAL_FILE, "r") as f:
                return self.send_text(f.read())

        # /accounts → return accounts.csv
        if parsed.path == "/accounts":
            if not os.path.exists(ACCOUNTS_FILE):
                return self.send_text("username,password\n")
            with open(ACCOUNTS_FILE, "r") as f:
                return self.send_text(f.read())

        # Default route → login page
        if parsed.path == "/" or parsed.path == "":
            return self.send_file(os.path.join(BASE_DIR, "login.html"))

        # Serve static files / documents from the main directory or policies-folder
        static_path = os.path.join(BASE_DIR, self.path[1:])
        if os.path.exists(static_path):
            return self.send_file(static_path)
            
        # Fallback check if the frontend is trying to download directly from the policies folder
        policy_path = os.path.join(POLICY_FOLDER, self.path[1:])
        if os.path.exists(policy_path):
            return self.send_file(policy_path)

        self.send_error(404, "Not found")

    def do_POST(self):
        parsed = urlparse(self.path)

        # Handle Preflight OPTIONS request if modern browsers check permissions
        if self.command == 'OPTIONS':
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "*")
            self.end_headers()
            return

        # /record_read → append to filereads.csv
        if parsed.path == "/record_read":
            length = int(self.headers["Content-Length"])
            data = self.rfile.read(length).decode()

            with open(READ_FILE, "a") as f:
                f.write(data)

            self.send_text("OK")
            return

        self.send_error(404, "Unknown POST endpoint")


server = HTTPServer(("", PORT), Handler)
print(f"Server running at http://localhost:{PORT}")
server.serve_forever()

