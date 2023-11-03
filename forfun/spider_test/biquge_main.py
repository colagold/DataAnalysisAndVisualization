# -*- coding: utf-8 -*-
# @Time    : 2023/10/21 10:49
# @Author  : colagold
# @FileName: biquge_main.py
import re

import requests
from bs4 import BeautifulSoup
headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
def get_html(url,headers):
    response=requests.get(url,headers=headers)
    if response.ok:
        print("响应成功")
        # print(response.text)
    else:
        print(response.status_code)
        print("响应失败")
    content=response.text
    return BeautifulSoup(content,"html.parser")

url_chapter_novel="https://www.xbiquge.bz/book/6281/4072981.html"
novel_home_page=get_html(url_chapter_novel,headers)
title=novel_home_page.find("div",attrs={"class": "bookname"}).h1.string
content=novel_home_page.select("#content")[0].text

# 使用正则进行替换
content = re.sub('\s+', '\r\n\t', content).strip('\r\n')
print(title)
print(content)
