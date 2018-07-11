# -*- coding: utf-8 -*-

import jieba.analyse
from pyecharts import WordCloud

f = open('anjuke_house_pingjia.txt','r',encoding = "utf-8").read()
str = {}
f = jieba.cut(f)

for w in f:
    if len(w) > 1:
        previous_count = str.get(w,0)
        str[w] = previous_count+1

list_x = []
list_y = []
for item in str.keys():
    list_x.append(item)
    list_y.append(str[item])

print(list_x,list_y)


# 词云
wordcloud = WordCloud(width=1600, height=1000)
wordcloud.add("", list_x, list_y, word_size_range=[20, 100])
# wordcloud.show_config()
wordcloud.render()
# import matplotlib.pyplot as plt #画图
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.show()