# -*- coding: utf-8 -*-

# 网贷点评 -  网贷中心 平台列表
# http://www.wdzx.com/plugin.php?id=dz55625_dianping:dianping&page=1
# http://www.wdzx.com/plugin.php?id=dz55625_dianping:dianping&ps=f&page=2
# http://www.wdzx.com/plugin.php?id=dz55625_dianping:dianping&page=69


import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd

# 返回请求 bsObj
def getHtmlbsObj(url):
    #http请求头
    Hostreferer = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Referer': 'http://www.wdzx.com/plugin.php'
        }
    start_html = requests.get(url, headers=Hostreferer)
    start_html.encoding = 'utf-8'
    bsObj = BeautifulSoup(start_html.text, "html.parser")
    return bsObj

info_list = list()
def getWDinfo(page):

    url = "http://www.wdzx.com/plugin.php?id=dz55625_dianping:dianping&page="+str(page)
    bsObj = getHtmlbsObj(url)
    # print(bsObj)
    all_div = bsObj.find("div",{"class":"listSj cl","id":"bh"}).find_all("dd",{"class":"xx"})
    # all_div_list = all_div
    # print(all_div)
    for item in all_div:

        temp = item.find("a")
        temp_p = item.find_all("p")
        # 名字
        title_url = "http://www.wdzx.com/"+str(temp.get('href'))
        getInfoByReurl(title_url)
        print(title_url)

    return info_list

def getInfoByReurl(url):
    bsObj = getHtmlbsObj(str(url))
    info_div_li_all = bsObj.find("div",{"class":"shangTop cl"}).find_all("li")

    title = info_div_li_all[0].strong.get_text()
    phone = info_div_li_all[3].font.get_text()
    official_website = info_div_li_all[4].a.get_text()
    address = info_div_li_all[6].get_text().replace("公司地址: ", "")

    temp_list = list()
    temp_list.append(title)
    temp_list.append(phone)
    temp_list.append(url)
    temp_list.append(official_website)
    temp_list.append(address)
    info_list.append(temp_list)
    print(title+"-"+phone+"-"+url+"-"+official_website+"-"+address)
    # for item in info_div_li_all:
    #     print(item)


if __name__ == '__main__':
    titles = ['公司','电话','网内链接','官网','地址']
    fileName = "D:/网贷中心_平台列表.csv"
    # 开始时间
    start = datetime.datetime.now()
    print(start)

    for item in range(1,69):
       list_s =  getWDinfo(str(item))
    # print(list_s.__len__())

    print("写入cvs格式文件")
    print(list_s.__len__())
    test = pd.DataFrame(columns=titles, data=list_s)
    test.to_csv(fileName)
    # 完成时间
    end = datetime.datetime.now()
    print(end)
    print("写入完成")
    useSeconds = (end - start).total_seconds()  # 精确秒数
    print(useSeconds)