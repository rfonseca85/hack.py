import http.server
import socketserver

PORT = 80

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Capture and print cookies to the console
        if "Cookie" in self.headers:
            cookies = self.headers["Cookie"]
            print(f"Received cookies: {cookies}")
        else:
            print("No cookies found")
        
        # Respond to the client
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, World! Your cookies have been logged.")
    
    def log_message(self, format, *args):
        # Override to prevent printing to stderr
        return

# Set up and start the server
Handler = MyHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"Serving at port {PORT}")
httpd.serve_forever()
