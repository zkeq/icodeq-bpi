# coding:utf-8
from contextlib import redirect_stderr
from http.server import BaseHTTPRequestHandler
from time import time
from urllib.parse import unquote
import base64



def get_url():
    _list = [1,2,3]
    fauil = _list[4]
    time.sleep(3)
    redirect_url = "https://ik.imagekit.io/zkeq/like.jpg"
    return redirect_url


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("self.path:", self.path)
        redirect_url = get_url()
        self.send_response(308)  # vercel 只有 308 跳转才可以缓存 详情见官方文档
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('location', redirect_url)  # 这个是主要的
        self.send_header('Refresh', '0;url={}'.format(redirect_url))
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Redirecting to {} (308)'.format(redirect_url).encode('utf-8'))  # 这里无所谓
        return None