import requests
from bs4 import BeautifulSoup
headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
for index in range(0,250,25):
    response=requests.get(f"https://movie.douban.com/top250?start={index}",headers=headers)
    content=response.text
    soup=BeautifulSoup(content,"html.parser")
    all_titles=soup.findAll("span",attrs={"class": "title"})
    all_pingjia=soup.findAll("span",string=lambda text: text and '评价' in text)
    for title in all_titles:
        title_string=title.string
        if "/" not in title_string:
            print(title_string)
    for i in all_pingjia:
        print(i.string)
# if response.ok:
#     print("响应成功")
#     # print(response.text)
# else:
#     print(response.status_code)
#     print("响应失败")