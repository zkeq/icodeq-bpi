# -*- coding: UTF-8 -*-
# 具体例子看我那个 API 仓库
from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        path = self
        print("path:", self)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(str(path.__dir__()).encode('utf-8'))
        return
