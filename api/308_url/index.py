# coding:utf-8
from http.server import BaseHTTPRequestHandler
import requests
import redis
import json
from urllib.parse import unquote
import os
import base64

env_dist = os.environ
PASSWORD = env_dist.get('PASSWORD')

r = redis.Redis(
    host='apn1-destined-giraffe-32369.upstash.io',
    port=32369,
    password=PASSWORD, ssl=True)


def get_video(_url, _cache, url_form):
    _str_base64 = base64.b64decode(url_form)
    data = r.get(_url)
    if data is None:
        data = requests.get(_url).content
        r.set(_url, data, ex=_cache)
        data = json.loads(data)
    else:
        data = data.decode('utf-8')
        data = json.loads(data)
    data_content = eval(_str_base64)
    return data_content


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        _form = self.path.split('?')[1]
        url = unquote(_form.split('url=')[1]).split('&')[0]
        cache = _form.split('cache=')[1].split('&')[0]
        _url_form = _form.split('form=')[1].split('&')[0]
        params_data = get_video(url, cache, _url_form)
        self.send_response(308)  # vercel 只有 308 跳转才可以缓存 详情见官方文档
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('location', params_data)  # 这个是主要的
        self.send_header('Refresh', '0;url={}'.format(params_data))
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Redirecting to {} (308)'.format(url).encode('utf-8'))  # 这里无所谓
        return None