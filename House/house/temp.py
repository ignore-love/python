# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re


#http请求头
Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
    }

start_html = requests.get("http://unicitytiankongzhichengwk.fang.com/", headers=Hostreferer)
bsObj = BeautifulSoup(start_html.text, "html.parser")


link_vas = bsObj.find("div", {"id": "orginalNaviBox", "class": "navleft tf"}) #
# 详情链接
info_link_temp = link_vas.find("a", {"id": "xfptxq_B03_08", "target": "_self"}).get('href')
# 户型链接
houseTypeLink  = link_vas.find("a", {"id": "xfptxq_B03_10", "target": "_self"}).get('href')

# 点评链接
dianping_links = link_vas.find("a",{"id":"xfptxq_B03_17","target":"_self"})

print(info_link_temp)
print(houseTypeLink)
print(dianping_links)
info_lists = list()
def getHouseInfo(link,typelink):
    info_list = list()

    # 详情页采集
    start_html = requests.get(link, headers=Hostreferer)
    start_html.encoding = 'gb18030'
    bsObj = BeautifulSoup(start_html.text, "html.parser")



    title = bsObj.find("a",{"class":"ts_linear","id":""}).get_text()
    # print("品名:"+title)
    # .strip() 去除空格
    price = bsObj.find("div",{"class":"main-info-price"}).em.get_text().strip()
    # print("价格:"+price)
    # 用户点评
    pingjias = bsObj.find("div",{"class":"main-info-comment"}).get_text().replace("\n", "").replace("\t", "").split(" ")[1].split("[")[0]
    # print("用户点评:"+pingjias)

    # 户型
    str_Type = huxingcaiji(typelink)
    info_list.append(title)
    info_list.append(str_Type)
    info_list.append(price)
    info_list.append(pingjias)


    # info_house["品名"] = title
    # info_house["价格"] = price
    # info_house["用户点评"] = pingjias
    # info_str = title+","+price+","+pingjias+","


    # 基本信息
    info_1 = bsObj.find_all("ul",{"class":"list clearfix"})
    # print(info_1)
    for temp in info_1:
        infotype = temp.find_all("div",{"class":"list-left"})
        infotype_1 = temp.find_all("div",{"class":"list-right"})
        # print(infotype+"---"+infotype_1)
        for x, y in zip(infotype, infotype_1):
            key = re.sub('[\t\n]', "", re.sub(r'<[^>]+>', "", str(x))).replace("：", "")
            values = re.sub('[\t\n]', "", re.sub(r'<[^>]+>', "", str(y))).replace(" ", "").replace("普通住宅:", "")
            info_list.append(values)

            # print(key+":"+values)

        # 小区规划
    info_2 = bsObj.find_all("ul",{"class":"clearfix list"})
    for temp in info_2:
        infotype = temp.find_all("div",{"class":"list-left"})
        infotype_1 = temp.find_all("div",{"class":"list-right"})
        # print(infotype+"---"+infotype_1)
        for x, y in zip(infotype, infotype_1):
            key = re.sub('[\t\n]', "", re.sub(r'<[^>]+>', "", str(x))).replace("：", "")
            values = re.sub('[\t\n]', "", re.sub(r'<[^>]+>', "", str(y))).replace(" ", "").replace("\xa0", "")
            # for item in values:
            if values == " " or values == "":
                values = "-"
            info_list.append(values)
    info_lists.append(info_list)
    return  info_lists


def huxingcaiji(typelink):
    # 户型页采集
    start_html = requests.get(typelink, headers=Hostreferer)
    start_html.encoding = 'gb18030'
    bsObj = BeautifulSoup(start_html.text, "html.parser")
    # 户型
    hTypeName = bsObj.find_all("p",{"class":"tiaojian"})  # .find_all("span",{"class":"fl"})
    # print(hTypeName)
    # HRs = bsObj1.find("ul",{"id":"ListModel","class":"clearfix  List_imglist"}).find_all("span",{"class":"fr"})
    str_Type = ""
    for temp in hTypeName:
        # print(temp)
        infotype = temp.find_all("span", {"class": "fl"})
        infotype_1 = temp.find_all("span", {"class": "fr"})
        for n, r in zip(infotype, infotype_1):
            str_Type =str_Type + n.get_text() + " " + r.get_text() + "\t"

    print(str_Type)
            # print(r.get_text())
    return str_Type




# getHouseInfo(info_link_temp,houseTypeLink)
print(huxingcaiji(houseTypeLink))

