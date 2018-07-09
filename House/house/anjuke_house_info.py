# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd
# 安居客  上海  新房 信息采集
# https://sh.fang.anjuke.com/loupan/all/p1/

titles = ['品名','楼盘首页','楼盘详情','户型','相册','用户点评','问答','地图交通','楼盘房源','动态资讯','楼盘评测', '看图链接']
url_lists = list()

# 返回请求 bsObj
def getHtmlbsObj(url):
    #http请求头
    Hostreferer = {
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
        }
    # url = "https://sh.fang.anjuke.com/loupan/all/p" + str(page) + "/"
    start_html = requests.get(url, headers=Hostreferer)
    start_html.encoding = 'utf-8'
    bsObj = BeautifulSoup(start_html.text, "html.parser")
    return bsObj


# 主存储链接
pages = list()


def getHouseTitleLink(page):
    num = 1
    url = "https://sh.fang.anjuke.com/loupan/all/p"+str(page)+"/"
    bsObj = getHtmlbsObj(url)
    h_div = bsObj.find_all("div", {"class": "infos"})
    if h_div != None:
    # print(h_link)
        for link in h_div:
            status = link.find("div",{"class":"tag-panel"}).i.get_text()
            #去除 售罄 的 楼盘
            if status != "售罄":
                name =  link.find("span",{"class":"items-name"}).get_text()
                if name not in pages:
                        print(str(num)+":"+name)
                        nameurl = getByNameFindUrl(name)
                        pages.append(name)
                        # print(pages)
            num = num+1
    else:
        print("h_div data is None  ERROR")
    return pages


# 返回一个详情页面
def getByNameFindUrl(name):
    # for name in NameLists:
    nameurl = ""
    # print(name)
    url = "https://sh.fang.anjuke.com/loupan/s?kw="+name

    # 搜索结果页
    bsObj = getHtmlbsObj(url)
    h_div = bsObj.find_all("div", {"class": "infos"})
    if h_div != None:
        for h_link in h_div:
            # https://sh.fang.anjuke.com/loupan/426516.html?from=AF_RANK_1
            # https://sh.fang.anjuke.com/loupan/426516.html?from=AF_RANK_13424
            nameurl = h_link.find("a", {"class": "lp-name"}).get('href')
            list_urls = getPageInfoUrl(nameurl)
            url_lists.append(list_urls)
            # print(nameurl)
    else:
        print("h_div_name data is None  ERROR")

    # # 右侧 更多  的url
    # left_hot_loupan = bsObj.find("div",{"class":"tuangou_entry s-mod"})
    # # <a>更多</a>  的 url
    # if left_hot_loupan != None:
    #     order_loupan_link = left_hot_loupan.find("a",{"class":"chk-more","soj":"loupan_list"})
    #     str = order_loupan_link.get_text() + ":" + order_loupan_link.get("href")
    #     print("75"+str)
    # else:
    #     print("left_hot_loupan data is None  ERROR")

    # # 下侧 热门新盘推荐  url
    # down_rec_loupan = bsObj.find_all("div",{"class":"item-mod"})
    # # print(down_rec_loupan)
    # if down_rec_loupan != None:
    #     for item in down_rec_loupan:
    #         loupan_div_all = item.find_all("div",{"class":"infos"})
    #         for item in loupan_div_all:
    #             # 标题
    #             loupan_name = item.find("span",{"class":"items-name"}).get_text()
    #             loupan_name_link = item.find("a",{"class":"lp-name"}).get("href")
    #             name_str = loupan_name + ":" +loupan_name_link
    #             print(name_str)
    #             # 地址
    #             loupan_address_link = item.find("a",{"class":"address"}).get("href")
    #             loupan_address_map = item.find("span",{"class":"list-map"}).get_text()
    #             address_str = loupan_address_map +":"+ loupan_address_link
    #             print(address_str)
    # else:
    #     print("down_rec_loupan data is None  ERROR")
    # return nameurl


 # 解析详情页面链接所有  url
def getPageInfoUrl(nameurl):
    links_url = list()
    if nameurl != None:
        bsObj = getHtmlbsObj(nameurl)

        # 楼盘名
        title = bsObj.find("div",{"class":"lp-tit"}).find("h1",{"id":"j-triggerlayer"}).get_text()
        links_url.append(title)
        print("title:"+title)
         # 解析 nav 导航采集 链接
        lp_nav_div = bsObj.find("div",{"class":"lp-nav"})
        nav_a_links = lp_nav_div.find_all("a")
        for temp in nav_a_links:
            a_link = temp.get('href')
            links_url.append(a_link)
            a_name = temp.get_text()
            str = a_name + ":" + a_link
            print("113"+str)

        # 看图链接
        img_link_div = bsObj.find("div",{"class":"clip"})
        if img_link_div != None:
            link = img_link_div.find("a").get("href")
            links_url.append(link)
            print("119看图链接:"+link)
        else:
            print("img_link_div data is None  ERROR")

        # 右侧url信息采集
        left_info_div = bsObj.find("div",{"class":"basic-details"})
        # if left_info_div != None:
            # find_a = left_info_div.find_all("a")
            # for item in find_a:
            #     str_title = item.get_text()
            #     str_url = item.get("href")
            #     print(str_title+":"+str_url)

        # else:
        #     print("left_info_div data is None  ERROR")
    else:
        print("nameurl data is None  ERROR")
    return links_url


if __name__ == '__main__':

    # 开始时间
    start = datetime.datetime.now()
    print(start)
    fileName = "D:/anjuke_house_url.csv"

    for i in range(1,10):
        lists = getHouseTitleLink(str(i))
    print(lists.__len__())

    print("写入cvs格式文件")
    print(url_lists.__len__())
    test = pd.DataFrame(columns=titles, data=url_lists)
    test.to_csv(fileName)
    # 完成时间
    end = datetime.datetime.now()
    print(end)
    print("写入完成")
    useSeconds = (end - start).total_seconds()  # 精确秒数
    print(useSeconds)