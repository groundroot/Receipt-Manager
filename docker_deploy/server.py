import http.server
import socketserver
import queue
import urllib.parse
import os

PORT = 8000
clients = []

class SyncHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/events':
            self.send_response(200)
            self.send_header('Content-type', 'text/event-stream')
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('Connection', 'keep-alive')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            q = queue.Queue()
            clients.append(q)
            try:
                self.wfile.write(b"data: connected\n\n")
                self.wfile.flush()
                while True:
                    msg = q.get()
                    self.wfile.write(f"data: {msg}\n\n".encode('utf-8'))
                    self.wfile.flush()
            except Exception as e:
                pass
            finally:
                if q in clients:
                    clients.remove(q)
        elif self.path == '/mobile' or self.path == '/mobile.html':
            self.path = '/mobile.html'
            return super().do_GET()
        elif self.path == '/' or self.path == '/index.html':
            self.path = '/index.html'
            return super().do_GET()
        else:
            return super().do_GET()

    def do_POST(self):
        if self.path == '/upload':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            # Broadcast to PC clients
            payload = post_data.decode('utf-8')
            for q in clients:
                q.put(payload)
                
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'{"success": true}')
        else:
            self.send_response(404)
            self.end_headers()

class ThreadedHTTPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == "__main__":
    server = ThreadedHTTPServer(("", PORT), SyncHandler)
    print(f"==================================================")
    print(f"✅ 스마트폰 사진 동기화 서버 시작됨 (포트: {PORT})")
    print(f"PC 링크: http://localhost:8000")
    print(f"스마트폰 뷰 연동 대기 중...")
    print(f"==================================================")
    server.serve_forever()
