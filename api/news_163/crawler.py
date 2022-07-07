# coding: utf-8
from bs4 import BeautifulSoup
import requests
import time


def get_days(index):
    list_url = 'https://www.163.com/dy/media/T1603594732083.html'
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
    }

    data = requests.get(list_url, headers=headers)
    print(data)
    print(data.text)
    soup = BeautifulSoup(data.text, 'lxml')
    days_list = soup.find_all('a', attrs={"class": "title"})
    new_url = days_list[index]['href']
    new_data = requests.get(new_url, headers=headers)
    soup = BeautifulSoup(new_data.text, 'lxml')
    day_news = soup.find('div', attrs={"class": "post_body"})
    list_all = str(day_news).split('<br/>')
    final_list = []
    num = 0
    for i in list_all:
        if "<" not in i and ">" not in i and i != '':
            i.replace('\u200b', '')
            final_list.append(i)
    return final_list


def main(index):
    try:
        data = get_days(index)
        suc = True
    except Exception as e:
        data = e
        suc = False
    return {
        'suc': suc,
        'time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        'data': {
            'title': data[0],
            'date': data[1],
            'news': data[2:-1],
            'weiyu': data[-1]
        },
        'all_data': data
    }
