# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

#http请求头
Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
    }
url = "http://en.wikipedia.org/wiki/kevin_Bacon"



def getLink(word):
    start_html = requests.get("http://en.wikipedia.org"+word, headers=Hostreferer)
    bsObj = BeautifulSoup(start_html.text, "html.parser")
    # html = urlopen("http://en.wikipedia.org"+word)
    # bsObj = BeautifulSoup(html)
    results = re.compile("^(/wiki/)((?!:).)*$")
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=results)

links = getLink("/wiki/Kevin_Bacon")

while len(links) > 0:
    newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticle)
    links=getLink(newArticle)