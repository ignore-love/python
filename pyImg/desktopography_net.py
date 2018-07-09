# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
# import re

# http://www.netbian.com/weimei/index_2.htm
# http://www.netbian.com/weimei/index_72.htm
# 壁纸

def getHtmlbsObj(url):
    #http请求头
    Hostreferer = {
        # 'Host':'desktopography.net',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        # 'Referer':'http://desktopography.net/exhibition-2010/'
        }
    # url = "https://sh.fang.anjuke.com/loupan/all/p" + str(page) + "/"
    start_html = requests.get(url, headers=Hostreferer)
    start_html.encoding = 'gbk'
    bsObj = BeautifulSoup(start_html.text, "html.parser")
    return bsObj

all_list = list()
def getImgInfo(page):
    url = "http://www.netbian.com/weimei/index_"+str(page)+".htm"
    bsObj = getHtmlbsObj(url)
    # print(bsObj)
    all_div = bsObj.find("div",{"class":"list"}).ul
    print(all_div)
    img_div = all_div.find_all("li")
    # print(img_div)
    for item in img_div:
        img_a = item.find("a",{"target":"_blank"})
        if img_a != None:
            img_url = img_a.get("href")
            all_list.append(img_url)
            print("35"+img_url)

def getImgUrl():
    for url in all_list:
        bsObj = getHtmlbsObj(url)
        all_div = bsObj.find("div",{"class":"wpPSCList"})
        # img_xx_div = all_div.find_all("a")  #[2].get("href")
        img_li = all_div.find_all("li") #[6].a.get("href")
        templist = list()
        for item in img_li:
            imgurl = item.a.get("href")
            templist.append(imgurl)
    print(templist)
    # for img_xx_div in img_xx_div:
    #     img_a = img_xx_div.find("a",{"class":"wallpaper-button","download":"ks_1920x1080.jpg"})
    #     imgurl = img_a.get("href")
    #     print(imgurl)


if __name__ == '__main__':
    getImgInfo(2)
    getImgUrl()

# def getHtml(url):
#     page = urllib.urlopen(url)  #urllib.urlopen()方法用于打开一个URL地址
#     html = page.read() #read()方法用于读取URL上的数据
#     return html

#
# def getImg(html):
#     reg = r'src="(.+?\.jpg)" pic_ext'    #正则表达式，得到图片地址
#     # imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
#     imglist #= re.findall(imgre,html)      #re.findall() 方法读取html 中包含 imgre（正则表达式）的    数据
#     # #把筛选的图片地址通过for循环遍历并保存到本地
#     # #核心是urllib.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
#     # x = 0
#
#     for imgurl in imglist:
#         urllib.urlretrieve(imgurl,'D:\img\%s.jpg' % x)
#         x+=1


# html = getHtml("http://tieba.baidu.com/p/xxxx")
# print (getImg(html))