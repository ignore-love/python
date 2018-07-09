# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup


def getbsOBj(url):
    html = urlopen(url)
    bsOBj = BeautifulSoup(html)
    return bsOBj


if __name__ == '__main__':
    url = "http://www.pythonscraping.com/pages/warandpeace.html"
    bsOBJ = getbsOBj(url)
    nameList = bsOBJ.find_all("span",{"class":"green"})
    for name in nameList:
        print(name.get_text())
    print("================================")
    txts = bsOBJ.find_all(id="text")
    # for txt in txts:
    print(txts)