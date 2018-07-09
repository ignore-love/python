# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd

# http://sh.to8to.com/company/list_1.html
# http://sh.to8to.com/company/list_2.html

# 返回请求 bsObj
def getHtmlTobsObj(url):
    #http请求头
    Hostreferer = {
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
        }
    # url = "https://sh.fang.anjuke.com/loupan/all/p" + str(page) + "/"
    start_html = requests.get(url, headers=Hostreferer)
    start_html.encoding = 'utf-8'
    bsObj = BeautifulSoup(start_html.text, "html.parser")
    return bsObj


# 条件
def getNav_title():
    titles = list()
    typename = list()
    typeurl = list()
    contents = list()

    url = "http://sh.to8to.com/company/list_1.html"
    bsObj = getHtmlTobsObj(url)
    nav_div = bsObj.find("div",{"class":"zgs_select_type"}).find_all("dl",{"class":"zgs_st_dl"})
    for item in nav_div:
        # 类型标签
        title = item.dt.get_text()
        titles.append(title)
        # 类型内容 + url
        str = ""
        flag = 1
        for t_u_div in item.dd.find_all("a"):

            content = t_u_div.get_text()
            typename.append(content)

            t_url = t_u_div.get("href")
            typeurl.append(t_url)

            if flag == 3:
                contents.append(typename)
                contents.append(typeurl)
                typename = list()
                typeurl = list()
            flag = flag + 1

            str =str + content +":" + t_url +"|"

        print(title+":"+str)
    # titles = ['装修公司', '电话号码', '链接', '设计案例', '装修工地']
    fileName = "D:/tubatu_type_url.csv"
    print("写入cvs格式文件")
    print(titles)
    print(contents.__len__())
    print(contents)
    test = pd.DataFrame(columns=titles, data=contents)
    test.to_csv(fileName)


contents = list()
def getName_tel_url(page):

    temp_list = list()
    url = "http://sh.to8to.com/company/list_"+str(page)+".html"
    bsObj = getHtmlTobsObj(url)
    content_div = bsObj.find("div",{"class":"company__list"})
    # print(content_div)
    if content_div != None:
        find_li = content_div.find_all("div",{"class":"company__data"})
        if find_li != None:
            for item in find_li:
                t_name = item.p.find("a").get_text()
                t_url = item.p.find("a").get("href")
                if item.find("p",{"class":"company__phone"}) != None:
                    t_tel = item.find("p",{"class":"company__phone"}).get_text().replace('-', '')
                else:
                    t_tel = "0"
                print(t_name+":"+t_tel+":"+t_url)




                temp_list = list()
                temp_list.append(t_name)
                temp_list.append(t_tel)
                temp_list.append(t_url)

                order_info = item.find("div", {"class": "company__data__show"}).find_all("span")
                for item in order_info:
                    str_temp = item.get_text().split("：")
                    print(str_temp[0]+":"+str_temp[1])
                    temp_list.append(str_temp[1])
                contents.append(temp_list)
            else:
                print("find_li is None ! ERROR")
    else:
        print("content_div is None ! ERROR")
    return contents




if __name__ == '__main__':
    getNav_title()
    for item in range(1,30):
        getName_tel_url(item)
    titles = ['装修公司','电话号码','链接','设计案例','装修工地']
    fileName = "D:/tubatu_type_url.csv"
    print("写入cvs格式文件")
    print(titles)
    print(contents.__len__())
    print(contents)
    test = pd.DataFrame(columns=titles, data=contents)
    test.to_csv(fileName)