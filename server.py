"""Fabula: serves index.html and keeps projects/styles as JSON files in data/."""
import json
import os
import re
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).parent
PORT = 5002


class Handler(BaseHTTPRequestHandler):
    def send(self, code, body=b"", ctype="application/json"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def route(self):
        # /api/<kind>[/<id>]; the id charset keeps paths inside data/
        m = re.fullmatch(r"/api/(projects|styles)(?:/([a-z0-9]+))?", self.path)
        if not m:
            return None, None
        folder = ROOT / "data" / m[1]
        folder.mkdir(parents=True, exist_ok=True)
        return folder, m[2] and folder / f"{m[2]}.json"

    def do_GET(self):
        if self.path == "/":
            return self.send(200, (ROOT / "index.html").read_bytes(), "text/html; charset=utf-8")
        folder, file = self.route()
        if not folder:
            return self.send(404)
        if file:
            return self.send(200, file.read_bytes()) if file.exists() else self.send(404)
        files = sorted(folder.glob("*.json"), key=lambda f: f.stat().st_mtime, reverse=True)
        items = [{"id": f.stem, "name": json.loads(f.read_bytes()).get("name") or f.stem} for f in files]
        self.send(200, json.dumps(items).encode())

    def do_PUT(self):
        _, file = self.route()
        if not file:
            return self.send(404)
        body = self.rfile.read(int(self.headers["Content-Length"]))
        try:
            json.loads(body)
        except ValueError:
            return self.send(400)
        # write-then-rename so a crash never leaves a half-written manuscript
        tmp = file.with_suffix(".tmp")
        tmp.write_bytes(body)
        os.replace(tmp, file)
        self.send(204)

    def do_DELETE(self):
        _, file = self.route()
        if file and file.exists():
            file.unlink()
        self.send(204)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"Fabula is running at http://localhost:{PORT}  (Ctrl+C to quit)")
    webbrowser.open(f"http://localhost:{PORT}")
    server.serve_forever()
