# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup#用于解析网页
import requests
import urllib.request
import re
#导入xlwt模块
import xlwt

url = "https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=monline_4_dg&wd=%E8%A3%85%E4%BF%AE&oq=%25E8%25A3%2585%25E4%25BF%25AE&rsv_pq=e52406080001ce1d&rsv_t=cfd0bIh0P4akzpTiJNZ8R%2BPYxPBC%2BjbxhdP2AwmkRvbq9mQRYBgNXonfo15oBSK8fz8p&rqlang=cn&rsv_enter=0&prefixsug=%25E8%25A3%2585%25E4%25BF%25AE&rsp=0"


# 创建一个Workbook对象，这就相当于创建了一个Excel文件
book = xlwt.Workbook(encoding='utf-8', style_compression=0)

sheet = book.add_sheet('url', cell_overwrite_ok=True)

#http请求头
Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    # 'Referer':'http://sh.ganji.com'
    }


def getUrl():
    # ul = 'http://sh.ganji.com/zhuangxiu/o' + str(page) + '/'
    start_html = requests.get(url, headers=Hostreferer)
    soup = BeautifulSoup(start_html.text, "html.parser")
    # print(soup)
    # phone = soup.find('span', class_='J_tel_phone_span')
    # dr = re.compile(r'<[^>]+>', re.S)
    # dd = dr.sub('', str(phone))
    # print(dd[2])
    # tel = dd.split(",")
    # print(tel)
    all_a = soup.find_all('div', class_='3003').find_all('a', target='_blank')
    # print(all_a)
    i = 1
    for t2 in all_a:
        i += 1
        t3 = t2.get('href')
        print(t3)
        sheet.write(i, 0, t3)
    # print(t3)

if __name__ == '__main__':
    # reload(sys);
    # sys.setdefaultencoding('utf8');
    # f = open('gongsi.csv', 'w');
    for j in range(1,15):
        getUrl();
    book.save(r'e:\Url_bd.xls')
    # s = """
    # </span><span style= 'font-size:12.0pt;color:#CC3399'>714659079qqcom    2014/09/10 10:14</span></p></div>
    # """
    # dr = re.compile(r'<[^>]+>', re.S)
    # dd = dr.sub('', s)
    # print(dd)