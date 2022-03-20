# coding:utf-8
import base64

data = {"data": [{"id": 1916523816,
                  "url": "http://m8.music.126.net/20220318104300/222ebf34c4779a739ba5d389c5e1592d/ymusic/obj/w5zDlMODwrDDiGjCn8Ky/12923448274/dcf7/42e2/ae73/988adcfda162524da13df7e0a24cc93f.flac",
                  "br": 687389, "size": 168580389, "md5": "988adcfda162524da13df7e0a24cc93f", "code": 200, "expi": 1200,
                  "type": "flac", "gain": 0, "fee": 0, "uf": None, "payed": 0, "flag": 0, "canExtend": False,
                  "freeTrialInfo": None, "level": None, "encodeType": None, "freeTrialPrivilege": None,
                  "freeTimeTrialPrivilege": {"resConsumable": False, "userConsumable": False, "type": 0,
                                             "remainTime": 0}, "urlSource": 0}], "code": 200}

url_form = 'ZGF0YVsiZGF0YSJdWzBdWyJ1cmwiXQ=='

_str_base64 = base64.b64decode(url_form)
normal_url = eval(_str_base64)

print(_data)
