# -*- coding: utf-8 -*-
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import time
import json

# 评价链接 ： https://sh.fang.anjuke.com/loupan/dianping-249038.htmls/   ?p=2
# url?p=num


# def getHtmlByUrl(data):
#     # 这里有三个注意的点：
#     # 1. mode="a"
#     # 2. "{}\n" 一条结果一行
#     # 3. ensure_ascii=False
#     # 我没怎么在python3下处理编码的问题，我试了一下你的代码不能正确输出中文
#     # 得加上ensure_ascii=False
#     with open ("bencao_detail2", mode="a", encoding='utf8') as file:
#         file.write("{}\n".format(json.dumps(data, ensure_ascii=False)))
#
#
# q = list(range(1, 1771))  #构造一个简单的队列，起始是1
#
# while len(q):  # 队列还有就执行
#     n = q.pop(0)  # 取出队列的第一个
#     print("Fetching No.{}".format(n))  # 这里输出到哪一步了，可以帮助你从断点处重来
#     url_api = "http://api.jisuapi.com/bencao/detail?appkey=bdc8ee0bb0227112&detailid={n}&isdetailed={n}".format(n=n)
#     try:
#         r = requests.get (data,timeout=3.05)
#     except Exception as e:
#         print("Exception: {}".format(e))
#         q.append(n)  # 出错放回到队列尾部
#     else:
#         data = r.json()
#         print(data)
#         getHtmlByUrl(data)
#     time.sleep(2)  # 还是设置一个等待吧，太快的访问容易被屏蔽。可以自己改


q = list(range(1, 90000))  #构造一个简单的队列，起始是1
def getHtmlByUrl(url):
    n = q.pop(0)  # 取出队列的第一个
    print("Fetching No.{}".format(n))  # 这里输出到哪一步了，可以帮助你从断点处重来
    # http请求头
    Hostreferer = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
    }
    try:
        start_html = requests.get(url, headers=Hostreferer, timeout=3.05)
        start_html.encoding = 'utf-8'
    except Exception as e:
        print("Exception: {}".format(e))

        q.append(n)  # 出错放回到队列尾部
        getHtmlByUrl(url)
    time.sleep(1)  # 还是设置一个等待吧，太快的访问容易被屏蔽。可以自己改
    bsObj = BeautifulSoup(start_html.text, "html.parser")
    return bsObj



list_url = []
def getTitleforUrl():
    csv_file = csv.reader(open("anjuke_house_url.csv",'r'))
    for item in csv_file:
        url = item[5]
        list_url.append(url)
    return list_url


list_content = []
def getInfobyHtml(item_url):
    for page in range(1,16):
        pingjia_url = item_url+'?p='+str(page)
        bsObj = getHtmlByUrl(pingjia_url)
        div_all = bsObj.find('div',{'class':'total-wrap'})
        if div_all != None:
            user_div = div_all.find_all('div',{'class':'info-mod'})
            for item_user in user_div:
                list_temp = []
                user_name = item_user.find('span',{'class':'author'}).get_text()
                user_text = item_user.find('h4',{'class':'rev-subtit all-text'}).get_text()
                list_temp.append(user_name)
                list_temp.append(user_text)
                list_content.append(list_temp)
                print(list_temp)
        else:
            print("此页无评价，结束！")
            return
    return list_content


if __name__ == '__main__':

    # 开始时间
    start = datetime.datetime.now()
    print(start)
    fileName = "D:/anjuke_house_pingjia.csv"
    titles = ['user','content']


    pingjia_list = getTitleforUrl()
    for item in pingjia_list:
        getInfobyHtml(item)


    print("写入cvs格式文件")
    print('评论数：',list_content.__len__())
    test = pd.DataFrame(columns=titles, data=list_content)
    test.to_csv(fileName)


    # 完成时间
    end = datetime.datetime.now()
    print(end)
    print("写入完成")
    useSeconds = (end - start).total_seconds()  # 精确秒数
    print(useSeconds)