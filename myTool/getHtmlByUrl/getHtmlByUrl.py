# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time
# class LOL_Spider(object):
#     def __init__(self, url):
#         self.url = url

class getHtmlByUrl(object):
    NUM = list(range(1, 90000))  #构造一个简单的队列，起始是1
    def __init__(self, url):
        self.url = url
        
    def getHtml(self):
        n = self.NUM.pop(0)  # 取出队列的第一个
        print("Fetching No.{}".format(n))  # 这里输出到哪一步了，可以帮助你从断点处重来
        # http请求头
        Hostreferer = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
        }
        try:
            start_html = requests.get(str(self.url), headers=Hostreferer, timeout=3.05)
            start_html.encoding = 'utf-8'
        except Exception as e:
            print("Exception: {}".format(e))

            self.NUM.append(n)  # 出错放回到队列尾部
            getHtmlByUrl(self.url)
        time.sleep(1)  # 还是设置一个等待吧，太快的访问容易被屏蔽。可以自己改
        bsObj = BeautifulSoup(start_html.text, "html.parser")
        return bsObj
    
    
    def getToHtml(self):
        bsObj = self.getHtml()
        return bsObj
    
    