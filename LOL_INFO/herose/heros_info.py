# -*- coding: utf-8 -*-

import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import time
import random
import re

# def getHtmlbsObj(url):
#     #http请求头
#     Hostreferer = {
#
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#         'Accept-Encoding': 'gzip, deflate, sdch',
#         'Accept-Language': 'zh-CN,zh;q=0.8',
#         'Connection': 'keep-alive',
#         'Cookie': 'eas_sid=X1d5i3Z1Z8F9n6U556S451t952; pgv_pvi=3496150016; pgv_si=s6453888000; ied_rf=lol.qq.com/web201310/info-heros.shtml; pgv_pvid=4478189360; pgv_info=pgvReferrer=&ssid=s3116820680; gpmtips_cfg=%7B%22iSendApi%22%3A0%2C%22iShowCount%22%3A0%2C%22iOnlineCount%22%3A0%2C%22iSendOneCount%22%3A0%2C%22iShowAllCount%22%3A0%2C%22iHomeCount%22%3A0%7D',
#         'Host': 'lol.qq.com',
#         'If-Modified-Since': 'Wed, 18 Jul 2018 07:10:00 GMT',
#         'Referer': 'http://lol.qq.com/web201310/info-spell.shtml',
#         'Upgrade-Insecure-Requests':'1',
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
#
#
#         # 'Connection':'keep - alive',
#         # 'Host':'lol.qq.com',
#         # 'Upgrade - Insecure - Requests':'1',
#         # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
#         }
#     # url = "https://sh.fang.anjuke.com/loupan/all/p" + str(page) + "/"
#     start_html = requests.get(url, headers=Hostreferer)
#     # time.sleep(3)  # 还是设置一个等待吧，太快的访问容易被屏蔽。可以自己改
#     start_html.encoding = 'gb2312'
#     bsObj = BeautifulSoup(start_html.text, "html.parser")
#
#     return bsObj

#
# def getHeros_info():
#     # url = 'http://ams.game.qq.com/log?sCloudApiName=atm'
#     url = 'http://lol.qq.com/web201310/info-heros.shtml'
#
#     bsObj = getHtmlbsObj(url)
#
#     all_div_ul = bsObj.find('ul',{'id':'jSearchHeroDiv','class':'imgtextlist'})
#     all_li = all_div_ul.find_all('li')
#     for item in all_li:
#         print(item)
#
#

# 第一步：获取js字典
def path_js(url_js):
    res_js = requests.get(url_js, verify = False).content
    html_js = res_js.decode("gbk")
    pat_js = r'"keys":(.*?),"data"'
    enc = re.compile(pat_js)
    list_js = enc.findall(html_js)
    dict_js = eval(list_js[0])
    return dict_js

# 第二步：从 js字典中提取到key值生成url列表
def path_url(dict_js):
    pic_list = []
    for key in dict_js:
        for i in range(20):
            xuhao = str(i)
            if len(xuhao) == 1:
                num_houxu = "00" + xuhao
            elif len(xuhao) == 2:
                num_houxu = "0" + xuhao
            numStr = key+num_houxu
            url = r'http://ossweb-img.qq.com/images/lol/web201310/skin/big'+numStr+'.jpg'
            pic_list.append(url)
    print(pic_list)
    return pic_list

# 第三步：从 js字典中提取到value值生成name列表
def name_pic(dict_js, path):
    list_filePath = []
    for name in dict_js.values():
        for i in range(20):
            file_path = path + name + str(i) + '.jpg'
            list_filePath.append(file_path)
    return list_filePath


# 第四步：下载并保存数据
def writing(url_list, list_filePath):
    try:
        for i in range(len(url_list)):
            res = requests.get(url_list[i], verify=False).content
            with open(list_filePath[i], "wb") as f:
                f.write(res)
    
    except Exception as e:
        print("下载图片出错,%s" % (e))
        return False


# 执行主程序：
if __name__ == '__main__':
    url_js = r'http://lol.qq.com/biz/hero/champion.js'
    path = r'E:/LOLpic/'
    dict_js = path_js(url_js)
    url_list = path_url(dict_js)
    list_filePath = name_pic(dict_js, path)
    writing(url_list, list_filePath)


# if __name__ == '__main__':
#     # getHeros_info()