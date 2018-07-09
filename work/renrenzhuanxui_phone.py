# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 列表网  家装装饰
# http://sh.renrzx.com/zxgs/?page=1
# http://sh.renrzx.com/zxgs/?page=153
# 返回请求 bsObj
def getHtmlbsObj(url):
    #http请求头
    Hostreferer = {
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
        }
    # url = "https://sh.fang.anjuke.com/loupan/all/p" + str(page) + "/"
    start_html = requests.get(url, headers=Hostreferer)
    start_html.encoding = 'gb2312'
    bsObj = BeautifulSoup(start_html.text, "html.parser")
    return bsObj

namephone = list()
def getNameAndPhone(page):
    url = "http://sh.renrzx.com/zxgs/?page="+str(page)
    bsObj = getHtmlbsObj(url)
    # all_li_div = bsObj.find("div",{"class":"m_main fl border"}).find_all("li")
    all_div = bsObj.find_all("span",{"class":"l_txt fl"})
    # 将正则表达式编译成Pattern对象
    # pattern = re.compile('\w<i>电话：</i>\w')
    if all_div != None:
        for item in all_div:
            templist = list()
            # print(item)
            name = item.find("a",{"target":"_blank"}).get_text()
            address = item.find_all("p")[2].get_text().replace('公司地址：', '')
            phone = item.find_all("p")[3].get_text().replace('电话：', '')
            print(name+"--"+address+"--"+phone)
            templist.append(name)
            templist.append(address)
            templist.append(phone)
            namephone.append(templist)
            # print(name)
    else:
        print("all_li_div is None !")
    return namephone

if __name__ == '__main__':

    titles = ['公司','地址','电话']
    fileName = "D:/人人家装网_上海电话.csv"
    for page in range(1,154):
        lists = getNameAndPhone(page)
    # print(lists)
    print("写入cvs格式文件")
    print(lists.__len__())
    test = pd.DataFrame(columns=titles, data=lists)
    test.to_csv(fileName)
    print("写入cvs格式文件 成功！")



