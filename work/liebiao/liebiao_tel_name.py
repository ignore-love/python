# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd

# 列表网  家装装饰
# http://shanghai.liebiao.com/zhuangxiu/index1.html
# http://shanghai.liebiao.com/zhuangxiu/index2.html

# 返回请求 bsObj
def getHtmlbsObj(url):
    #http请求头
    Hostreferer = {
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
        }
    # url = "https://sh.fang.anjuke.com/loupan/all/p" + str(page) + "/"
    start_html = requests.get(url, headers=Hostreferer)
    start_html.encoding = 'utf-8'
    bsObj = BeautifulSoup(start_html.text, "html.parser")
    return bsObj

titleList = list()
def getTitleLink(page):

    url = "http://shanghai.liebiao.com/zhuangxiu/index"+str(page)+".html"
    bsObj = getHtmlbsObj(url)
    alltitle_div = bsObj.find("div",{"class":"post-list"})
    li_div_all = alltitle_div.find_all("li",{"class":"post clf"})
    for item in li_div_all:
        templist = list()
        title_info = item.find("div", {"class":"post-title-wrap"}).find("a",{"class":"text-highlight"})
        title_phone_div = item.find("div", {"class":"contact-box"}).find("button",{"class":"btn-contact"})
        phone = title_phone_div.get("data-phone")
        name = title_info.get_text()
        link = title_info.get('href')
        templist.append(name)
        templist.append(phone)
        titleList.append(templist)
    # title_info = alltitle_div.find_all("div",{"class":"post-title-wrap"})
    # title_phone_div = alltitle_div.find_all("div",{"class":"contact-box"})
    # for item,item1 in zip(title_info,title_phone_div):
    #     title_a = item.find("a",{"class":"text-highlight"})
    #     title_phone = item1.find("button",{"class":"btn-contact"})
    #     name = title_a.get_text()
    #     link = title_a.get('href')
    #     phone = title_phone.get("data-phone")
    #     # if str(phone).__len__() < 11:
    #     templist.append(name)
    #     templist.append(phone)
        print(name +":"+link+":"+phone)





if __name__ == '__main__':

    titles = ['公司','电话']
    fileName = "D:/列表网家装电话.csv"
    for page in range(1,40):
        getTitleLink(page)
        # print(titleList)
    print("写入cvs格式文件")
    print(titleList.__len__())
    test = pd.DataFrame(columns=titles, data=titleList)
    test.to_csv(fileName)
    print("写入cvs格式文件 成功！")
