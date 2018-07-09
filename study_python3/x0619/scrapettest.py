# -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except(HTTPError,URLError) as e:
        return None
    try:
        bsOBJ = BeautifulSoup(html.read())
        title = bsOBJ.h4
    except ArithmeticError as e:
        return None
    return title

if __name__ == '__main__':
    url = "https://blog.csdn.net/qq_34708892"
    title = getTitle(url)
    if title == None:
        print("Title could not be found")
    else:
        print(title)
# print(bsOBJ.h4)