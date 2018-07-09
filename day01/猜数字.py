# -*- coding: utf-8 -*-
import random

flag=random.randint(1,100)
print (flag)
a=int(input("猜一个0~100的数字："))

buff = True
while buff:
    if a==flag:
        print("bingo! 猜对了 我想的也是",flag)
        buff = False
    elif a>flag:
        print("erro! 错了哦 你猜小一点")
        a = int(input("猜一个0~10的数字："))
    elif a < flag:
        print("erro! 错了哦 你猜大一点")
        a = int(input("猜一个0~10的数字："))


















