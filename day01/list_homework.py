# -*- coding: utf-8 -*-
list1 = ['1','2',3,4,'wu']
print(type(list1))
print("------------------------------------")

# 增加
list1.append("傻子")
print(list1)
print("------------------------------------")

#合并
list2 = list1 + [12,358,'ewq','fsdf','nijap']
print(list2)
print("------------------------------------")

#删除
del list1[2]
print(list1)
print("------------------------------------")

#修改
list1[0] = "holle word"
print(list1)
print("------------------------------------")

# 遍历
for item in list1:
    print(item)
print("------------------------------------")


#截取 从下标为 1 截取到下标为 3（两个）
list3 = list2[1:3]
for item in list3:
    print(item)
print("------------------------------------")












