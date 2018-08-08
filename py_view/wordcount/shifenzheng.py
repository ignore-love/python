# -*- coding: UTF-8 -*-
import os

# 获取需要处理的数据
f = open('shifenzheng.txt', 'r', encoding='gbk')  # 只读，要处理的数据
# 写数据
ff = open('m数据.txt', 'a')  # 追加形式，写入新建文件
b = 0
c = set()  # set集合，集合元素是不重复的
# 大量数据时用readline(一条)，readlines(全部)
while 1:
    l = f.readline()
    a = l.split("\t")
    b = b + 1
    c.add(a[0] + "\n")
    print(a[0])
    if l == '':
        break
print(b)
aa = list(c)
aa.sort()
# 写入数据
for bb in aa:
    ff.write(bb)

f.close()
ff.close()