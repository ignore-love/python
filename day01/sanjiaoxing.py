# -*- coding: utf-8 -*-

print("输入三角形三边：")
a=int(input("输入边长a："))
b=int(input("输入边长b："))
c=int(input("输入边长c："))
# print(a,b,c)

if a+b>c and a+c>b and c+b>a:
    print("三角形边长为：",a,b,c)

    if a==b or b==c or a==c :
        print("三角形边长为等腰三角行：", a, b, c)
    if (a**2+b**2)==c**2 or (a**2+c**2)==b**2 or (c**2+b**2)==a**2 :
        print("三角形边长为直角三角行：", a, b, c)

else:
    print("不合法输入！")

















