# -*- coding: utf-8 -*-
# http://newhouse.sh.fang.com/house/s/b91/?ctm=1.sh.xf_search.page.1
import requests
from bs4 import BeautifulSoup
import re
# import csv
import pandas as pd
import datetime
import time
# 房天下  上海  新房 信息采集
# http://newhouse.sh.fang.com/house/s/澜庭
# 主存储链接
pages = set()

#http请求头
Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
    }


# 正则匹配房型链接
results = re.compile("http://[^www][A-Za-z0-9]{9,50}\.fang\.com[^*]$")
def getHouseLink(page):
    # 获取房子网页
    url = "http://newhouse.sh.fang.com/house/s/b9"+str(page)+"/?ctm=1.sh.xf_search.page.1"
    start_html = requests.get(url, headers=Hostreferer)
    bsObj = BeautifulSoup(start_html.text, "html.parser")
    h_link = bsObj.find_all("a",{"target":"_blank","href":results})
    for link in h_link:
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newpage = link.attrs['href']
                print(newpage)
                pages.add(newpage)
    return pages


# 更多详细信息 url
HousesInfoLinks = set()
# 解析房型页面<更多详细信息 url>链接
def getHouseInfoLink(houselinks):
    for link in houselinks:
        start_html = requests.get(link, headers=Hostreferer)
        bsObj = BeautifulSoup(start_html.text, "html.parser")

        link_vas = bsObj.find("div", {"id": "orginalNaviBox", "class": "navleft tf"})  #

        # 品名链接
        house_name_link = link
        # 详情链接
        info_link_temp = link_vas.find("a",{"id":"xfptxq_B03_08","target":"_self"})
        # 户型链接
        houseTypeLink = link_vas.find("a",{"id":"xfptxq_B03_10","target":"_self"})
        # 点评链接
        dianping_links = link_vas.find("a",{"id":"xfptxq_B03_17","target":"_self"})

        # print("58行品名链接"+house_name_link)
        # print("59行详情链接" + info_link_temp)
        # print("60行户型链接" + houseTypeLink)
        # print("61行点评链接" + dianping_link)

        if info_link_temp == None or houseTypeLink == None or dianping_links == None :
            print("Title could not be found")
        else:
            infolink = info_link_temp.get('href')
            typelink = houseTypeLink.get('href')
            dianping_link = dianping_links.get('href')
            print(infolink+typelink)
            if infolink not in pages:
                    # newpage = infolink
                    print(infolink)
                    temps = getHouseInfo(house_name_link,infolink,typelink,dianping_link)
                    if temps == None:
                        print("------------------")
                    else:
                        HousesInfoLinks.add(infolink)
    return HousesInfoLinks





# 更多详细信息 url
# dict = {}
# 解析房型详细信息页面 获取 基本信息 销售信息 小区规划 价格信息
# http://yuhushangyuanxh021.fang.com/house/1210125570/housedetail.htm

# 定义类型接收
# info_str = " "

titles = ['品名','户型','价格','用户点评', '品名链接','详情链接','户型链接','点评链接','看房团链接','物业类别', '项目特色', '建筑类别', '装修状况', '产权年限', '环线位置', '销售状态', '楼盘优惠', '开盘时间', '交房时间', '售楼地址', '咨询电话', '占地面积', '建筑面积', '容积率', '绿化率', '停车位', '楼栋总数', '总户数', '物业公司', '物业费']

info_lists = list()
def getHouseInfo(house_name_link,link,typelink,dianping_link):
    info_list = list()

    # 详情页采集
    start_html = requests.get(link, headers=Hostreferer)
    start_html.encoding = 'gb18030'
    bsObj = BeautifulSoup(start_html.text, "html.parser")

    # #户型页采集
    # start_html1 = requests.get(typelink, headers=Hostreferer)
    # start_html1.encoding = 'gb18030'
    # bsObj1 = BeautifulSoup(start_html1.text, "html.parser")

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
    # 用户点评
    info_list.append(pingjias)

    # 链接
    # '品名链接', '详情链接', '户型链接', '点评链接

    # 品名链接
    info_list.append(house_name_link)
    # 详情链接
    info_list.append(link)
    # 户型链接
    info_list.append(typelink)
    # 点评链接
    info_list.append(dianping_link)

    # 看房团链接
    temp_looks = bsObj.find("div",{"id":"sjina_C13_08","class":"contentHot"}).find_all("a",{"class":"btn-sign"})
    look_link = ""
    if temp_looks == None:
        print("look Link is None")
    else:
        for item in temp_looks:
            link = item.get('href')
            look_link = look_link + "|" + link +"|"
        # return look_link
    info_list.append(look_link)


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
        # print(info_2)

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
            str_Type =str_Type + n.get_text() + " " + r.get_text() + "|"
    return str_Type



if __name__ == '__main__':
    # 开始时间
    start = datetime.datetime.now()
    print(start)
    fileName = "D:/Fang_house_info_type_url.csv"
    for i in range(1,2):
        getHouseLink(i)
    print(pages.__len__())
    urlSet = getHouseInfoLink(pages)
    print(urlSet.__len__())
    print("写入cvs格式文件")
    print(info_lists)
    test = pd.DataFrame(columns=titles,data=info_lists)
    test.to_csv(fileName)
    # 完成时间
    end = datetime.datetime.now()
    print(end)
    print("写入完成")
    useSeconds = (end - start).total_seconds()  # 精确秒数

    print(useSeconds)
    # link = "http://yishengyuzhonghuan.fang.com/house/1210125824/housedetail.htm"
    # link_type = "http://yishengyuzhonghuan.fang.com/photo/list_900_1210125824.htm"
    #
    # lists = getHouseInfo(link, link_type)
    #
    # print(lists)
    # fileName = "D:/Fang_house_info.csv"

    # # values list集合
    # valuesList = list()
    # for i in range(1,2):
    #     getHouseLink(i)
    #     print(i)
    # print(pages.__len__())
    # urlSet = getHouseInfoLink(pages)
    # print(urlSet.__len__())
    # # for link in urlSet:
    #     print(link)
    #     getHouseInfo(link)
        # if getHouseInfo(link) == None:
        #     print("-------------")
        # else:
        #     print(titles)
            # print(info_lists)
        # print(house_info)
    # print("写入cvs格式文件")
    # test = pd.DataFrame(columns=titles,data=info_lists)
    # test.to_csv(fileName)






        # getHouseInfo(link)
        # 写csv文件    print("写入一些简单数据到csv_dict_data.csv文件中")
        # with open("test.csv", "w") as csvfile:
        #     writer = csv.writer(csvfile)
        # 先写入columns_name
        # writer.writerow(["index", "a_name", "b_name"])
        # # 写入多行用writerows
        # writer.writerows([[0, 1, 3], [1, 2, 3], [2, 3, 4]])

 # for key in dicts.keys():
        #     valuesList.append(dicts[key])
        #     print(valuesList)
        #     with open(fileName, "w") as csvFile:
        #         writer = csv.writer(csvFile)
        #         writer.writerows(dicts[key])
        #         print("已写入  --> " + dicts[key])
        # csvFile.close()
