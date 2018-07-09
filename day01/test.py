# import this
# print("你是说我在哪里")
#
# a = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,14,17)
# for b in a:
#     print(b)
#
#
# sites = ["Baidu", "Google","Runoob","Taobao"]
# for site in sites:
#     if site == "Runoob":
#         print("菜鸟教程!")
#         break
#     print("循环数据 " + site)
# else:
#     print("没有循环数据!")
# print("完成循环!")

# a = 3
# b = 3
# print(id(a))
# print(id(b))
# b=5
# print(a)
# print(id(a))
# print(id(b))
# List=5
#
# for i in range(5):
#     print(i)
# list = range(0,100,5).count()
#
# print(type(list))
# for i in list:
#     print(i)
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, '等于', x, '*', n//x)
#             break
#     else:
#         # 循环中没有找到元素
#         print(n, ' 是质数')
import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")