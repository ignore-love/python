# -*- coding: utf-8 -*-
import csv
from pyecharts import WordCloud
from pyecharts import Bar


list_address = []
def getCSV():

    csv_file = csv.reader(open('Fang_house_info_type_url.csv', 'r'))
    for item in csv_file:
        str_list = item[14]
        list_address.append(str_list)
    return list_address

def wordcount(list_address):
    count_dict = {}
    list_x = []
    list_y = []
    for str in list_address:
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
    a,b = wordcount(getCSV())
    # 柱形表
    bar = Bar("房天下_户型图表", "**************")
    # bar = Bar("我的第一个图表", "这里是副标题")
    bar.add("楼盘户型", a, b)
    bar.show_config()
    bar.render()

    # 词云
    # wordcloud = WordCloud(width=1300, height=620)
    # wordcloud.add("", a, b, word_size_range=[20, 100])
    # wordcloud.show_config()
    # wordcloud.render()