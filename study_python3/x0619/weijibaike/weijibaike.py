# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

#http请求头
Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
    }
url = "http://en.wikipedia.org/wiki/kevin_Bacon"

# 获取网页
start_html = requests.get(url, headers=Hostreferer)
bsObj = BeautifulSoup(start_html.text, "html.parser")

# find <a></a>
a_s = bsObj.find_all("a")

# 正则过滤
results = re.compile("^(/wiki/)((?!:).)*$")

# 过滤无用的a标签
a_s_s = bsObj.find("div",{"id":"bodyContent"}).find_all("a",href=results)


for link in a_s_s:
    if 'href' in link.attrs:
        print(link.attrs['href'])