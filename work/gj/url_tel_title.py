# -*- coding: utf-8 -*-
import re
# from urllib import request
import urllib3
#http请求头
header = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
}


#
# def get_contents(page):
#     url = 'http://sh.ganji.com/zhuangxiu/o' + str(page) + '/'
#     #user-agent头
#     headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT6.1; Trident/5.0"}
#     req = urllib3.Request(url)
#     response = urllib3.urlopen(req)
#     html = response.read()
#     gbk_html = html.decode("gbk").encode("utf-8")
#     pattern = re.compile(r'<a.*?class="js_wuba_stas">(.*?)</a>', re.S)
#     item_list = pattern.findall(gbk_html)
#     print(item_list)


import urllib.request

file=urllib.request.urlopen('http://sh.ganji.com/zhuangxiu/o1/')

data=file.read()    #读取全部

dataline=file.readline()    #读取一行内容

pattern = re.compile(r'<a.*?class="js_wuba_stas">(.*?)</a>', re.S)
item_list = pattern.findall(dataline)
print(item_list)

# if __name__ == '__main__':
#     for j in range(1,10):
#         get_contents(str(j));
