# -*- coding: utf-8 -*-
import csv
# 读取csv文件
csv_file = csv.reader(open('Fang_house_info_type_url.csv','r'))

type_list = []

for item in csv_file:
    str_list = item[1].split('|')
    for item in str_list:
        str_list = item.split(" ")
        list_temp = list()
        list_temp.append(str_list[0])
        list_temp.append(1)
        type_list.append(list_temp)

        # print(str_list[0])
print(type_list)

wordcount = list()

# for item in type_list:
#     # wordcount.append(it)

print(wordcount)
