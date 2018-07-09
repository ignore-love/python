from urllib.request import urlopen#用于获取网页
from bs4 import BeautifulSoup#用于解析网页
import requests
import urllib.request
import re
#导入xlwt模块
import xlwt

# 创建一个Workbook对象，这就相当于创建了一个Excel文件
book = xlwt.Workbook(encoding='utf-8', style_compression=0)

sheet = book.add_sheet('url', cell_overwrite_ok=True)


#http请求头
Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    # 'Referer':'http://sh.ganji.com'
    }



def getUrl(page):
    ul = 'http://sh.ganji.com/zhuangxiu/o' + str(page) + '/'
    start_html = requests.get(ul, headers=Hostreferer)
    soup = BeautifulSoup(start_html.text, "html.parser")
    # print(soup)
    phone = soup.find_all('span', class_='J_tel_phone_span')
    # dr = re.compile(r'<[^>]+>', re.S)
    # dd = dr.sub('', str(phone))
    print(phone)
    # tel = dd.split(",")
    # print(tel)
    all_a = soup.find_all('a', class_='js_wuba_stas') #.find_all('a', target='_blank')
    # print(all_a)
    i = 1
    # for t2 in all_a:
    #     i += 1
    #     t3 = t2.get('href')
    #     sheet.write(i, 0, t3,tel[i])
        # print(t3)




def getUrl1(page):
    BASE_URL = 'http://sh.ganji.com/zhuangxiu/o' + str(page) + '/'
    BOOK_LINK_PATTERN = '<a target="_blank" class="js_wuba_stas"  href="(http:/.*)">'

    req = urllib.request.Request(BASE_URL)
    html = urllib.request.urlopen(req)
    doc = html.read().decode('utf8')
    print(re.findall(BOOK_LINK_PATTERN, doc))
    #url_list = list(set(re.findall(BOOK_LINK_PATTERN, doc)))



if __name__ == '__main__':
    # reload(sys);
    # sys.setdefaultencoding('utf8');
    # f = open('gongsi.csv', 'w');
    for j in range(1,15):
        getUrl(str(j));
    # book.save(r'e:\Url_gj.xls')
    # s = """
    # </span><span style= 'font-size:12.0pt;color:#CC3399'>714659079qqcom    2014/09/10 10:14</span></p></div>
    # """
    # dr = re.compile(r'<[^>]+>', re.S)
    # dd = dr.sub('', s)
    # print(dd)