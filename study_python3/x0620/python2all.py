# -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

# 储存网站
pages = set()

# 时间作为随机数
random.seed(datetime.datetime.now())

# 获取页面所有没链的列表
def getInterLinks(bsObj,includeUrl):
    includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    interLink = []
    # 找出所有以"/"开头的链接
    for link in bsObj.find_all("a",href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] not in None:
            if link.attrs['href'] not in interLink:
                if(link.attrs['href'].startswith("/")):
                    interLink.append(includeUrl+link.attrs['href'])
                else:
                    interLink.append(link.attrs['href'])
    return interLink

# 获取页面所有外链的列表
def getExternalLinks(bsObj,excludeUrl):
    externalLinks = []
    # 找出所有以“http”或者以“www”开头切不包含当前URL的链接
    for link in bsObj.find_all("a",href = re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj,urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print("No external link！！！！")
        domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
        internalLinks = getInterLinks(bsObj,domain)
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is :"+externalLink)
    followExternalOnly(externalLink)



followExternalOnly("http://oreilly.com")


