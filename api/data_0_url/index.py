# coding:utf-8
from http.server import BaseHTTPRequestHandler
import requests
import redis
import json
import os

env_dist = os.environ
PASSWORD = env_dist.get('PASSWORD')

r = redis.Redis(
    host='apn1-destined-giraffe-32369.upstash.io',
    port=32369,
    password=PASSWORD, ssl=True)


def get_video(url, cache):
    data = r.get(url)
    if data is None:
        data = requests.get(url).content
        r.set(url, data, ex=cache)
        data = json.loads(data)
    else:
        data = data.decode('utf-8')
        data = json.loads(data)
    data_content = data.get('data')[0].get('url')
    return data_content


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = self.path.split('?')[1]
        cache = self.path.split('?')[2]
        params_data = get_video(url, cache)
        self.send_response(308)  # vercel 只有 308 跳转才可以缓存 详情见官方文档
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('location', params_data)  # 这个是主要的
        self.send_header('Refresh', '0;url={}'.format(params_data))
        self.send_header('Cache-Control', 'max-age=0, s-maxage=60, stale-while-revalidate=3600')  # vercel 缓存
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Redirecting to {} (308)'.format(url).encode('utf-8'))  # 这里无所谓
        return None
