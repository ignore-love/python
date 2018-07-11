# -*- coding: utf-8 -*-
import csv
import numpy as np
# from matplotlib.pyplot import
from pyecharts import Bar
from pyecharts import WordCloud
# 读取csv文件
# csv_file = csv.reader(open('Fang_house_info_type_url.csv','r'))
#
# type_list = []
#
# for item in csv_file:
#     str_list = item[1].split('|')
#     for item in str_list:
#         str_list = item.split(" ")
#         # list_temp = list()
#         # list_temp.append(str_list[0])
#         type_list.append(str_list[0])
#
#         # print(str_list[0])
# print(type_list)

def getTextbycsv():
    csv_file = csv.reader(open('Fang_house_info_type_url.csv', 'r'))

    type_list = []

    for item in csv_file:
        str_list = item[1].split('|')
        for item in str_list:
            str_list = item.split(" ")
                # list_temp = list()
                # list_temp.append(str_list[0])
            type_list.append(str_list[0])
    return type_list


def wordcount(type_list):
    count_dict = {}
    list_x = []
    list_y = []
    for str in type_list:
            if str in count_dict.keys():
                count_dict[str] = count_dict[str] + 1
            else:
                count_dict[str] = 1
        #按照词频从高到低排列
            # count_list=sorted(count_dict.iteritems(),key=lambda x:x[1],reverse=True)
    for item in count_dict.keys():
        list_x.append(item)
        list_y.append(count_dict[item])

    return list_x,list_y



if __name__ == '__main__':
    a,b = wordcount(getTextbycsv())
    print(a)
    print(b)
    # plt.plot(a,b,'go')
    # plt.show()

    # 柱形表
    bar =Bar("房天下_户型图表", "**************")
    # bar = Bar("我的第一个图表", "这里是副标题")
    bar.add("楼盘户型", a, b)
    bar.show_config()
    bar.render()

    #词云
    wordcloud = WordCloud(width=1300, height=620)
    wordcloud.add("", a, b, word_size_range=[20, 100])
    wordcloud.show_config()
    wordcloud.render()

    # wordcloud = WordCloud(width=1300, height=620)
    # wordcloud.add("", a, b, word_size_range=[30, 100], shape='diamond')
    # wordcloud.show_config()
    # wordcloud.render()