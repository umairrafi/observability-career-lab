"""Minimal Sentry relay stub — accepts envelope POSTs for lab week 5."""
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        _ = self.rfile.read(length)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'{"id":"mock-event"}')

    def log_message(self, fmt, *args):
        print(f"[mock-sentry] {args[0]}")


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
