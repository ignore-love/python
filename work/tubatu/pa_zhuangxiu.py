# -*- coding: utf-8 -*-
# http://sh.to8to.com/company/?keyword=%E8%A3%85%E4%BF%AE&location=1#show_company

from bs4 import BeautifulSoup#用于解析网页
import requests
# import urllib.request
# import re
# #导入xlwt模块
# import xlwt

# # 创建一个Workbook对象，这就相当于创建了一个Excel文件
# books = xlwt.Workbook(encoding='utf-8', style_compression=0)
# sheets = books.add_sheet('url', cell_overwrite_ok=True)

#http请求头
Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
    }

# 装修
zx = 'http://sh.to8to.com/company/?location=1&keyword=%E8%A3%85%E4%BF%AE&page=1'
# 装修公司
zxgs = 'http://sh.to8to.com/company/?location=1&keyword=%E8%A3%85%E4%BF%AE%E5%85%AC%E5%8F%B8&page=1'
# 家装
jz = 'http://sh.to8to.com/company/?location=1&keyword=%E5%AE%B6%E8%A3%85&page=1'

# 上海装修
shzx = 'http://sh.to8to.com/company/?location=1&keyword=上海装修&page=1'
# 执行
def getUrl(page):
    ul = 'http://sh.to8to.com/company/?location=1&keyword=上海装修&page='+str(page)
    start_html = requests.get(ul, headers=Hostreferer)
    soup = BeautifulSoup(start_html.text, "html.parser")
    # print(soup)
    # phone = soup.find_all('span', class_='J_tel_phone_span')
    # dr = re.compile(r'<[^>]+>', re.S)
    # dd = dr.sub('', str(phone))
    # print(phone)
    # tel = dd.split(",")
    # print(tel)
    # all_href = soup.find_all('a', class_='zgscl_logo') #.find_all('a', target='_blank')
    all_name = soup.find_all('a', class_='zgscl_name')  # .find_all('a', target='_blank')
    # all_name = soup.find_all('div', class_='special_service').find('em', target='_blank')
    # print(all_name)
    # i = 1
    for t2 in all_name:
        # i += 1
        urls = t2.get('href')
        names = t2.string
        print(names+"-----"+urls)
        # sheets.write(i, 0, names)
        # sheets.write(i, 1, urls)


if __name__ == '__main__':
    for i in range(1,6):
        getUrl(str(i));
    # books.save(r'e:\jz_Url_Name_top5.xls')