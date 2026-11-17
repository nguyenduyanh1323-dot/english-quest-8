#!/usr/bin/env python3
"""
English Quest 8 — máy chủ Python đơn giản (chỉ dùng thư viện chuẩn của Python).
Chạy:  python3 server.py
Sau đó mở trình duyệt tại: http://localhost:8000

Không chứa khóa API nào. Tiến độ học được lưu ngay trong trình duyệt
của học sinh (localStorage), máy chủ chỉ phục vụ file tĩnh.
"""
import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", "8000"))
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Cho phép PWA/service worker hoạt động và tránh cache cứng khi phát triển
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"English Quest 8 dang chay tai http://localhost:{PORT}")
        print("Nhan Ctrl+C de dung.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
