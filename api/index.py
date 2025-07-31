from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            'message': 'Hello from TMNT API',
            'path': self.path,
            'status': 'working'
        }
        
        self.wfile.write(json.dumps(response).encode())
        return