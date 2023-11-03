# -*- coding: utf-8 -*-
# @Time    : 2023/10/20 22:33
# @Author  : colagold
# @FileName: biquge.py
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

url_novel="https://www.xbiquge.bz/book/6281/"
novel_home_page=get_html(url_novel,headers)
all_content=novel_home_page.dl
for i in all_content.findAll('a'):
    print(f"{i.string} link {i.get('href')}")
titles=novel_home_page.findAll("dt")
chapters=novel_home_page.findAll("dd")

for title in all_content:
    title_string=title.string
    #if "/" not in title_string:
    print(title_string)

# # all_titles=soup.findAll("span",attrs={"class": "title"})
# # all_pingjia=soup.findAll("span",string=lambda text: text and '评价' in text)
# for title in all_titles:
#     title_string=title.string
#     if "/" not in title_string:
#         print(title_string)
# for i in all_pingjia:
#     print(i.string)
