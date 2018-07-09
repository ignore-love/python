# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

#http请求头
Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
    }
url = "http://www.pythonscraping.com/pages/page3.html"

# 获取网页
start_html = requests.get(url, headers=Hostreferer)
bsObj = BeautifulSoup(start_html.text, "html.parser")
# bsObj = BeautifulSoup(html,'html_parser')

# 获取子标签
childs = bsObj.find("table",{"id":"giftList"}).children

# 获取后代标签  TODO 子标签一定是后代标签，后代标签不一定是子标签
huodai = bsObj.find("table",{"id":"giftList"}).descendants

# 处理兄弟标签
siblings = bsObj.find("table",{"id":"giftList"}).tr.next_siblings


#正则 获取图片路劲

re_str = re.compile("\.\./img\/gifts\/img.*\.jpg")

imgdirs = bsObj.find_all("img",{"src":re_str})


# 打印
for child in imgdirs:
    print(child["src"])

