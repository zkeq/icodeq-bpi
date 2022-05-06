# -*- coding: UTF-8 -*-
# 具体例子看我那个 API 仓库
from http.server import BaseHTTPRequestHandler




class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        print("self.request:", self.request)
        data_content = self.request['data']
        headers = self.request.form['headers']
        data = eval(data_content)
        print("data:", data)
        headers = eval(headers)
        print("headers:", headers)
        table = get_table(data, headers)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(table)
        return
