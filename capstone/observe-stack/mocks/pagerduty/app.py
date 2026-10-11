"""PagerDuty Events API v2 stub — logs incoming alerts for week 7/9."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        try:
            payload = json.loads(body)
            print("[mock-pagerduty]", json.dumps(payload, indent=2)[:500])
        except json.JSONDecodeError:
            print("[mock-pagerduty] invalid json")
        self.send_response(202)
        self.end_headers()
        self.wfile.write(b'{"status":"accepted"}')

    def log_message(self, fmt, *args):
        pass


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
