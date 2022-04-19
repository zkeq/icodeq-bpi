# coding:utf-8

import requests
import execjs
import redis
import os
import time
import re


"""
运行本份代码需要搭建node.js环境
node需要安装crypto-js模块
"""

env_dist = os.environ
PASSWORD = env_dist.get('PASSWORD')

r = redis.Redis(
    host='apn1-destined-giraffe-32369.upstash.io',
    port=32369,
    password=PASSWORD, ssl=True)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}


def get_params(_pr, _pu, _url):
    with open('./api/parwix/get-new-url/decode.js', 'r', encoding='utf-8') as f:
        ctx = execjs.compile(f.read())
        dit = ctx.call('jie_mi', _pr, _pu, _url)
        return dit


def try_time_three(_url, TIMES):
    try:
        TIMES += 1
        datas = requests.get(_url, headers=headers).text
        print(_url, "获取到的数据为：", datas)
        re.findall('"url": "(.*?)", //视频链接', datas)[0]
    except (requests.exceptions.ConnectionError, IndexError) as e:
        if TIMES == 3:
            exit(404)
        print(f"遇到错误{e}，正在尝试第 {TIMES} 次重新获取数据")
        time.sleep(5)
        try_time_three(_url, TIMES)
    return datas


def get_data(before_url):
    base_url = 'https://jx.parwix.com:4433/player/analysis.php?v='
    final_url = base_url + before_url
    TIMES = 0
    datas = try_time_three(final_url, TIMES)
    url_ek = re.findall('"url": "(.*?)", //视频链接', datas)[0]
    _pr = re.findall('user-scalable=no" id="(.*?)">', datas)[0]
    _pu = re.findall('<meta charset="UTF-8" id="(.*?)">', datas)[0]
    return url_ek, _pr, _pu


def post_mv_2_redis(_video_id, _video_url):
    print('正在将获取到的视频地址放入 Redis 中: ', end=' ')
    print(r.set(_video_id, _video_url, ex=9000))
    return_url = r.get(_video_id)
    return return_url


if __name__ == '__main__':
    video_list = ['https://www.bilibili.com/video/BV1G5411o7yX']
    for i in video_list:
        url, pr, pu = get_data(i)
        data = get_params(pr, pu, url)
        print("本次尝试获取的视频地址为: " + i)
        print("获取到的数据为: ", data)
        post_mv_2_redis(i, data)
        print('-' * 100)
    print('执行完毕！')
