# -*- coding: utf-8 -*-
# from pyecharts import Bar
#
# bar = Bar("手机", "单位：W")
# ptoject = ["oppo r11", "oppo r15", "vivo x20", "m5", "iPhone 7", "iPhone X"] # 轴
# num = [500, 202, 363, 101, 754, 900]  # y 轴
# bar.add("产品", ptoject, num)
# # bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
# bar.render()    # 生成本地 HTML 文件


# from pyecharts import Line
#
# ptoject = ["oppo r11", "oppo r15", "vivo x20", "m5", "iPhone 7", "iPhone X"] # 轴
# num1 = [500, 202, 363, 101, 754, 900]  # y 轴
# num2 = [450, 302, 563, 431, 554, 780]
# line = Line("折线图示例")
# line.add("商家A", ptoject, num1, mark_point=["average"])
# line.add("商家B", ptoject, num2, is_smooth=True, mark_line=["max", "average"])
# line.render()


from pyecharts import WordCloud

wordcloud = WordCloud(width=1300, height=620)
WordCloud.add(
    name,         # name -> str  图例名称
    attr,         # attr -> list  属性名称
    value,        #value -> list  属性所对应的值
    shape="circle",  # shape -> list  词云图轮廓，有'circle', 'cardioid', 'diamond', 'triangle-forward', 'triangle', 'pentagon', 'star'可选
    word_gap=20,    # word_gap -> int  单词间隔，默认为 20。
    word_size_range=None,  # word_size_range -> list  单词字体大小范围，默认为 [12, 60]
    rotate_step=45)   # rotate_step -> int  旋转单词角度，默认为 45


# name -> str  图例名称
#
# attr -> list  属性名称
#
# value -> list  属性所对应的值
#
# shape -> list  词云图轮廓，有'circle', 'cardioid', 'diamond', 'triangle-forward', 'triangle', 'pentagon', 'star'可选
# word_gap -> int  单词间隔，默认为 20。
# word_size_range -> list  单词字体大小范围，默认为 [12, 60]。
# rotate_step -> int  旋转单词角度，默认为 45





name = [
    'Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications',
    'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp',
    'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham',
    'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
value = [
    10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112,
    965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265]
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[20, 100])
wordcloud.render()