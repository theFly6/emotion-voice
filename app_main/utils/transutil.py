import requests, time, re, js2py
import json
from fake_useragent import UserAgent

headers = {'User-Agent': UserAgent().random,
               'Refer': 'https://fanyi.baidu.com/',
               'Cookie': 'BAIDU_WISE_UID=wapp_1710689191193_833; BAIDUID=58D121ACB8DC5E6BECD3D9B48F796520:FG=1; BAIDUID_BFESS=58D121ACB8DC5E6BECD3D9B48F796520:FG=1; BDUSS=mdJMHIzZlctR2RxaWxWWnV5YXhxblBWM3dXZzNBekNnc2tCcVI2N1E0eFNLQjltRVFBQUFBJCQAAAAAAQAAAAEAAABu8hJEsKLLubbZuMG0q8bmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFKb92VSm~dlY; BDUSS_BFESS=mdJMHIzZlctR2RxaWxWWnV5YXhxblBWM3dXZzNBekNnc2tCcVI2N1E0eFNLQjltRVFBQUFBJCQAAAAAAQAAAAEAAABu8hJEsKLLubbZuMG0q8bmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFKb92VSm~dlY; BIDUPSID=58D121ACB8DC5E6BECD3D9B48F796520; PSTM=1710857337; H_WISE_SIDS=39662_40207_40211_40215_40320_40079_40364_40351_40378_40409_40416_40312_40305_40465_40459_40438; H_WISE_SIDS_BFESS=39662_40207_40211_40215_40320_40079_40364_40351_40378_40409_40416_40312_40305_40465_40459_40438; smallFlowVersion=old; APPGUIDE_10_7_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1711683168; RT="z=1&dm=baidu.com&si=75fc90a9-77d9-455a-af3e-7264dbcfa3de&ss=lui4x965&sl=i&tt=b7v&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=opzt&ul=pv20&hd=pv26"; H_PS_PSSID=40320_40079_40378_40416_40312_40305_40465_40459_40511_40512_40398_60042_60024_60031; ZFY=isLdjGrlgD42Qoq:Are:A57aga4sendfWRTHhF0j:B0hvo:C; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1712063157,1712118108,1712285627,1712488632; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1712488632; ab_sr=1.0.1_ODBiMTAxMWNkZTZlMjBhZTBmNzkxYmIxMTBlNWE0OTNkY2MwMjdjMzQ2ZTNiMjIxNTE0MTkzNjAxNTI4OGFkOWE3Mzk5YjM2NTA4NWY4Y2ZkOTk0OGI0YmYxOTI3M2NhMzgxY2FlMzdiYTVlMWU4YzVhZWUyM2MxN2Q2NDBmYTdhYmUwODJiYWFmOTJmNjRjMmQzMmRkMzUxNGFjM2IzY2NlYTVmY2VkMGI4MTQ0ZTEwM2FkYjBkYzA5MGY1NmQ5'}

token = 'fd3e2d0cef37c1dc12066484cfaed727'


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
    resp = requests.get('https://fanyi.baidu.com/', headers=headers)
    html_str = resp.content.decode()  # resp.text
    gtk = re.search(r'gtk = "(.*?)\"', html_str).group(1)
    # print('gtk: ',gtk)
    return gtk


def trans_word_fromA2B(from_lang, to_lang, word):

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
