# coding:utf-8
from http.server import BaseHTTPRequestHandler
import requests
import redis
import json
from urllib.parse import unquote
import os
from fake_useragent import UserAgent
import base64

env_dist = os.environ
PASSWORD = env_dist.get('PASSWORD')
COOKIE = env_dist.get('COOKIE')

r = redis.Redis(
    host='apn1-destined-giraffe-32369.upstash.io',
    port=32369,
    password=PASSWORD, ssl=True)

del PASSWORD

def get_video(_url, _cache, url_form):
    _str_base64 = base64.b64decode(unquote(url_form))
    print("_str_base64:", _str_base64)
    data = r.get(_url)
    print("try get data:", data)
    headers = {"User-Agent": UserAgent().chrome}
    print("headers:", headers)
    if data is None:
        print("data is None")
        data = requests.get(_url, headers=headers,cookies=COOKIE).content
        r.set(_url, data, ex=min(int(_cache), 3600))
        data = json.loads(data)
        print("data:", data)
    else:
        data = data.decode('utf-8')
        data = json.loads(data)
        print("data:", data)
    data_content = eval(_str_base64)
    print("data_content:", data_content)
    https_content = data_content.replace('http', 'https')
    return https_content


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("self.path:", self.path)
        _form = self.path.split('?')[1]
        print('_form:', _form)
        url = unquote(_form.split('url=')[1].split('&')[0])
        print('url:', url)
        cache = _form.split('cache=')[1].split('&')[0]
        print('cache:', cache)
        _url_form = _form.split('form=')[1].split('&')[0]
        print('_url_form:', _url_form)
        params_data = get_video(url, cache, _url_form)
        print('params_data:', params_data)
        self.send_response(308)  # vercel 只有 308 跳转才可以缓存 详情见官方文档
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('location', params_data)  # 这个是主要的
        self.send_header('Refresh', '0;url={}'.format(params_data))
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Redirecting to {} (308)'.format(url).encode('utf-8'))  # 这里无所谓
        return None