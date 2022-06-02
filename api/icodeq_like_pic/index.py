# coding:utf-8
from http.server import BaseHTTPRequestHandler
import time

pic_list = [
    "https://ik.imagekit.io/zkeq/like.jpg",
    "https://ik.imagekit.io/zkeq/2se.jpg",
    "https://bu.dusays.com/2022/06/02/6298cee04cb42.jpg"
]


def get_pic():
    # 获取当前的秒数
    now_time = time.time()
    # 获取当前的小时数
    now_hour = time.localtime(now_time).tm_hour
    now_time_mod = int(now_hour % len(pic_list))
    # 获取当前的秒数的余数的图片地址
    pic_url = pic_list[now_time_mod]
    return pic_url


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = get_pic()
        self.send_response(308) # vercel 只有 308 跳转才可以缓存 详情见官方文档
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('location', url) # 这个是主要的
        self.send_header('Refresh', '0;url={}'.format(url))
        self.send_header('Cache-Control', 'max-age=0, s-maxage=60, stale-while-revalidate=3600') # vercel 缓存
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Redirecting to {} (308)'.format(url).encode('utf-8'))  # 这里无所谓
        return None
