# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time
import datetime
import pandas as pd

# 安居客  租房  三室 3000-3500
# https://sh.zu.anjuke.com/fangyuan/fx3-p1-zj5338/
# https://sh.zu.anjuke.com/fangyuan/fx3-p50-zj5338/


# 返回请求 bsObj
def getHtmlbsObj(url):
    #http请求头
    Hostreferer = {
        'Referer':'https://sh.zu.anjuke.com/fangyuan/fx3-p1-zj5338/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
        }
    # url = "https://sh.fang.anjuke.com/loupan/all/p" + str(page) + "/"
    start_html = requests.get(url, headers=Hostreferer)
    start_html.encoding = 'utf-8'
    time.sleep(1.5)  # 还是设置一个等待吧，太快的访问容易被屏蔽。可以自己改
    bsObj = BeautifulSoup(start_html.text, "html.parser")
    return bsObj
    

fang_info_list = []
def getHtmlToUrllist(bsObj):
    # h_div = bsObj.find_all("div", {"class": "infos"})
    zu_info = bsObj.find_all("div",{"class":"zu-itemmod"})
    # print("29",zu_info)
    for item in zu_info:
        # print(item)
        a_link = item.find('a',{'class':'img','data-sign':'true'})
        url = a_link.get("href")
        print(url)
        if url not in fang_info_list:
            fang_info_list.append(url)
        
    
fang_info_all_list = []
def getHouseInfo(url):
    list_temp = []
    bsObj = getHtmlbsObj(url)
    ul_item = bsObj.find('ul',{'class':'house-info-zufang cf'})
    if ul_item != None:
        # 价格  押金
        price_type_div = ul_item.find('li',{'class':'full-line cf'})
        
        if price_type_div != None:
            
            price = price_type_div.find('span',{'class':'price'}).getText()
            type = price_type_div.find('span', {'class': 'type'}).getText()
            list_temp.append(price)
            list_temp.append(type)
            # print(price,type)

            li_item_1 = ul_item.find_all('li',{'class':'house-info-item l-width'})
            if li_item_1 != None:
                for item in li_item_1:
                    str_temp_span = item.find('span', {'class':'info'})
                    if str_temp_span == None:
                        print(" is None")
                        # return
                    else:
                        str_temp_1 = str_temp_span.getText()
                        list_temp.append(str_temp_1)
                        # print("59",str_temp_1)
            li_item_2 = ul_item.find_all('li', {'class':'house-info-item'})
            if li_item_2 != None:
                for item in li_item_2:
                    str_temp_span = item.find('span', {'class': 'info'})
                    if str_temp_span == None:
                        print(" is None")
                        # return
                    else:
                        str_temp_2 = str_temp_span.getText()
                        list_temp.append(str_temp_2)
                        # print("68", str_temp_2)
                fang_info_all_list.append(list_temp)
                print(list_temp)
    # print(price,type,)
    # for item in li_item:
    
 

def run():
    # 开始时间
    start = datetime.datetime.now()
    print(start)
    fileName = "D:/anjuke_house_url.csv"
    title = ['1','2','3','4','5','6','7','8','9','10','11']
    for num in range(1,51):
        print('正爬取第',num,"页 >>>>>>>>")
        bsObj = getHtmlbsObj("https://sh.zu.anjuke.com/fangyuan/fx3-p"+str(num)+"-zj5338/")
        getHtmlToUrllist(bsObj)
    for item,num in zip(fang_info_list,range(fang_info_list.__len__())):
        print("分析第",num,"家：->")
        getHouseInfo(item)
    print("写入cvs格式文件")
    print(fang_info_all_list.__len__())
    test = pd.DataFrame(columns=title, data=fang_info_all_list)
    test.to_csv(fileName)
    # 完成时间
    end = datetime.datetime.now()
    print(end)
    print("写入完成")
    useSeconds = (end - start).total_seconds()  # 精确秒数
    print(useSeconds)
   
        
if __name__ == '__main__':
    run()