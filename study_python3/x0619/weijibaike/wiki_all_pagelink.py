# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

results = re.compile("^(/wiki/)")

def getLinks(Url):
    global pages
    html = urlopen("http://en.wikipedia.org"+Url)
    bsObj = BeautifulSoup(html)
    for link in bsObj.find_all("a",href = results):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newpage = link.attrs['href']
                print(newpage)
                pages.add(newpage)
                getLinks(newpage)
getLinks("")