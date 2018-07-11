# -*- coding: utf-8 -*-
import csv
from pyecharts import WordCloud
from pyecharts import Bar
from pyecharts import Line
from pyecharts import Pie

list_type = []
list_are = []
def getCSV():
    csv_file = csv.reader(open('2nd_house_price.csv','r')) #.decode('utf-8')
    # fp = open('2nd_house_price.csv', 'rb')
    # content = fp.read().decode('utf-8')
    print(csv_file)
    for item in csv_file:
        str_list = item[6]
        str_are = item[2]
        list_type.append(str_list)
        list_are.append(str_are)
    return list_type,list_are


def wordcount(list_type):
    count_dict = {}
    list_x = []
    list_y = []
    for str in list_type:
        if str in count_dict.keys():
            count_dict[str] = count_dict[str] + 1
        else:
            count_dict[str] = 1
            # 按照词频从高到低排列
    # count_list=sorted(count_dict.iteritems(),key=lambda x:x[1],reverse=True)
    for item in count_dict.keys():
        list_x.append(item)
        list_y.append(count_dict[item])

    return list_x, list_y


def run():
    getCSV()
    a , b = wordcount(list_type)
    m, n = wordcount(list_are)
    # # 词云
    # wordcloud = WordCloud(width=1300, height=620)
    # wordcloud.add("", a, b, word_size_range=[20, 100])
    # wordcloud.show_config()
    # wordcloud.render()

    # 柱形表
    # bar = Bar("链家二手房_户型图表", "**************")
    # # bar = Bar("我的第一个图表", "这里是副标题")
    # bar.add("楼盘户型", a, b)
    # bar.show_config()
    # bar.render()

    # attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    # v1 = [11, 12, 13, 10, 10, 10]
    # pie = Pie("饼图示例")
    # pie.add("", a, b, is_label_show=True)
    # pie.show_config()
    # pie.render()

    # line = Line("折线图-面积图示例")
    # line.add("商家A", a, b, is_fill=True, line_opacity=2000000, area_opacity=4000000, symbol=None)
    # # line.add("商家B", m, n, is_fill=True, area_color='#000',line_opacity=200000, area_opacity=300000, symbol=None)
    # line.show_config()
    # line.render()

    line = Line("折线图示例")
    line.add("价格", a, b, mark_point=["average"])
    # line.add("", m, n, is_smooth=True, mark_line=["max", "average"])
    line.show_config()
    line.render()
    line = Line("折线图-阶梯图示例")
    line.add("价格", a, b, is_step=True, is_label_show=True)
    # line.add("商家A", attr, v1, is_step=True, is_label_show=True)
    line.show_config()
    line.render()


    # m, n = wordcount(list_address)
    # # 词云
    # wordcloud = WordCloud(width=1300, height=620)
    # wordcloud.add("", m, n, word_size_range=[20, 100])
    # wordcloud.show_config()
    # wordcloud.render()

if __name__ == '__main__':
    run()