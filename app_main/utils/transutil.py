import requests, time, re, js2py
import json
from fake_useragent import UserAgent

token = 'a16beed6b65fdd984564a4d7014db8cf'


def generate_sign(gtk, word):
    """生成sign"""
    # 1. 准备js编译环境
    context = js2py.EvalJs()
    with open('app_main/utils/transutil.js', encoding='utf8') as f:
        js_data = f.read()
        # js_data = re.sub("window\[l\]",'"'+gtk+'"',js_data)
        js_data = js_data.replace("window[l]", '"' + gtk + '"')
        context.execute(js_data)
    sign = context.e(word)
    # print('sign: ',sign)
    return sign


def get_gtk():
    '''获取token和gtk(用于合成Sign)'''
    resp = requests.get('https://fanyi.baidu.com/')
    html_str = resp.content.decode()  # resp.text
    gtk = re.search(r'gtk = "(.*?)\"', html_str).group(1)
    # print('gtk: ',gtk)
    return gtk


def trans_word_fromA2B(from_lang, to_lang, word):
    headers = {'User-Agent': UserAgent().random,
               'Cookie': 'BIDUPSID=6271A13ACA2CF71B67078FE18394E89C; PSTM=1629121143; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; SOUND_SPD_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=737388A5FCA6FD9C4DD95A025B17D1BA:FG=1; BAIDUID_BFESS=737388A5FCA6FD9C4DD95A025B17D1BA:FG=1; BAIDU_WISE_UID=wapp_1684368760889_770; BDUSS=mY2Z3hOWFVQT0tvMkY0SHlJalhPT2V6NGdaTGFZV2NHYTFIaUVxNFpXQm9hYXBrRVFBQUFBJCQAAAAAAQAAAAEAAABu8hJEsKLLubbZuMG0q8bmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGjcgmRo3IJkR; BDUSS_BFESS=mY2Z3hOWFVQT0tvMkY0SHlJalhPT2V6NGdaTGFZV2NHYTFIaUVxNFpXQm9hYXBrRVFBQUFBJCQAAAAAAQAAAAEAAABu8hJEsKLLubbZuMG0q8bmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGjcgmRo3IJkR; __bid_n=18be531eed1876847b850d; newlogin=1; ZFY=8cIEMgffxBeSvyk1xCiX7489btYe9IYD5mx0ZD4:AUzo:C; H_PS_PSSID=39996_40040_39661_40156_40159; BA_HECTOR=0h052g0k242ka020800h010ks1kr5c1ir3ri71s; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=2; kleck=4d0c013b4794bdc8f0eb545b538c1dc1; RT="z=1&dm=baidu.com&si=ea86d0bc-3cc4-449b-aace-69581a263b7b&ss=lrss7pv0&sl=1&tt=5ot&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=6hd&ul=75k&hd=75s"; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1704548958,1705911495,1706088960,1706168520; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1706168520; ab_sr=1.0.1_ODViZDcyNmE2MTM1MjVmNjZhZDkxMjZmN2MwMjZiNmM4YThmMjIzYTBiZTJkNGRlZjI2MGIyOTI3YzI1YTM0YTFkYTQxMDI1YjU0Y2ZlMDhhOTMxYzQ2YzdkZjI5NmM2MDRkODNiMjgzYjRhMTA3ZjEzZGVkMzg5ZGU0MTJiNGNmMWMwY2JhMWE1MjM4Mzc2ZWJmNDU0YzdiOTVhNmRmMWJjYjRlZThmOWJkMWRiYjAzZmJjZDk1MmYwYzk0ODY0Y2MzNDhiYWQ1YTBjODQ5OWVlZDU1NjBkOGNhMTk0ZTk3MjEyNjkwMGFhODI4M2Q0MmRmOWRhZmRiZDE3OWNlNA=='}

    url = 'https://fanyi.baidu.com/v2transapi?'
    data = {'from': from_lang,
            'to': to_lang,
            'query': word,
            # 'transtype': 'realtime',
            # 'simple_means_flag': '3',
            'sign': generate_sign(get_gtk(), word),
            'token': token,
            # 'domain': 'common',
            # 'ts': int(time.time())
            }

    r = requests.post(url, headers=headers, data=data)
    return r.json()['trans_result']['data'][0]['dst']
