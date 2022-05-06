# -*- coding: UTF-8 -*-
# 具体例子看我那个 API 仓库
from http.server import BaseHTTPRequestHandler


def get_table(data, headers):
    table = ''
    width = len(headers)
    head_p = []
    for i in headers:
        head_p.append(":----:")
    if headers:
        table += '|' + '|'.join(headers) + '|' + '\n'
        table += "|" + '|'.join(head_p) + '|'
    else:
        table = ''
    num = 0
    for row in data:
        if num % width == 0:
            table += "\n|"
        table += row + "|"
        num += 1
    print(table)
    return table


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        print("self.request:", self.request)
        data_content = self.request.form['data']
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
