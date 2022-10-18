import requests
import re
import json
import pandas as pd


def get_json_data(page):
    url = 'https://api.bilibili.com/x/v2/reply/main?'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
        "referer": "https://www.bilibili.com/video/BV1HR4y1775Z"
    }
    params = {
        'callback': 'jQuery17206752522958787988_1644651682110',
        'jsonp': 'jsonp',
        'next': page,
        'type': 1,
        'oid': 338896747,
        'mode': 2,
        'plat': 1,
        '_': 1644654903971
    }
    resp = requests.get(url, headers=headers, params=params)

    text = resp.text
    json_str = re.findall(r'\(({.*})\)', text)[0]
    json_data = json.loads(json_str)
    return json_data


data = get_json_data(1)['data']
# 总评论数
total = data['cursor']['all_count']
# 评论总页数
pages = total // 20
df = pd.DataFrame(columns=['id', 'content', 'ctime', 'like', 'uname', 'sex', 'mid'], dtype=object)
for page in range(pages):
    print(page)
    data = get_json_data(page)
    replies = data['data']['replies']
    for reply in replies:
        df = df.append({
            'id': reply['rpid'],
            'content': reply['content']['message'],
            'ctime': reply['ctime'],
            'like': reply['like'],
            'uname': reply['member']['uname'],
            'sex': reply['member']['sex'],
            'mid': reply['member']['mid'],
        },
            ignore_index=True
        )
df['ctime'] = pd.to_datetime(df['ctime'], unit='s') + pd.Timedelta(days=8 / 24)
df.drop_duplicates(inplace=True)
df.to_excel('50万彩礼.xlsx', index=None)