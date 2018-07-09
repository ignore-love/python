# -*- coding: utf-8 -*-
import requests
import re


# agent_url="http://sh.ganji.com/zhuangxiu/o3/"
# agent_url="http://sh.ganji.com/zhuangxiu/o4/"
#http请求头
header = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
}

def get_content(page):
    url = 'http://sh.ganji.com/zhuangxiu/o' + str(page) + '/'
    start_html = requests.get(url, headers=header)
    # html = a.read().decode('gbk')#读取源代码并转为unicode
    return start_html

if __name__ == '__main__':
    for j in range(1,10):
        htmls = get_content(str(j));
        # pattern = '<a.*?href="(.+)".*?>(.*?)</a>'
        # with open(get_content(str(j)), "r") as fp:
        #     for line in fp:
        #         ret = re.search(pattern, line)
        #         if ret:
        #             for x in ret.groups(): print
        #             x
        print(type(htmls))


# #http请求头
# Hostreferer = {
#     'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
#     'Referer':'http://www.mzitu.com'
#                }
# Picreferer = {
#     'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
#     'Referer':'http://i.meizitu.net'
# }
#
# #保存地址
# path = 'D:/GJurl_tel/'
#
# reg = re.compile(r'class="website fl js_wuba_stas">.*? <a target="_blank" title="(.*?)".*? <span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*? <span class="t5">(.*?)</span>',re.S)