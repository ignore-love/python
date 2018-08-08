# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


# x = np.linspace(0, 10, 100)
# plt.plot(x, np.sin(x))
# plt.title('a sine curve')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.show()



# 我们来画一个  f(x)=x^{3}+2x^{2}+3x+4 函数的图形：
#
# func = np.poly1d(np.array([1,2,3,4]).astype(float)) #生成指定的多项式
# x = np.linspace(-10,10,60) #获得自变量X的一个取值数组
# y = func(x)                #获得结果y的数组
# plt.plot(x,y)
# plt.xlabel('x')       #设置x轴标签
# plt.ylabel('y(x)')    #设置y轴标签
# plt.show()

# 我们再绘制 f(x)=x^{3}+2x^{2}+3x+4 的同时，再绘制其一阶导函数 f'(x)的图像。
# func = np.poly1d(np.array([1,2,3,4]).astype(float))
# func1 = func.deriv(1)
# x = np.linspace(-10,10,30)
# y = func(x)
# y1 = func1(x)
# plt.plot(x,y,':r', label='y=f(x)')
# plt.plot(x,y1,'-g', label=r"y=f'(x)")
# plt.legend()
# plt.show()

# 这里我们采用了颜色+线形的简单方法，我这里列举几个常用的：
# 实线（-）；虚线（--）；点划线（-.）；实点线（:）
# 绿色（g）；青色（c）；黑色（k）；红色（r）；蓝色（b）；黄色（y）



func = np.poly1d(np.array([1,2,3,4]).astype(float)) #原函数
func1 = func.deriv(1)                               #一阶导函数
func2 = func.deriv(2)                               #二阶导函数
x = np.linspace(-10,10,30)
y = func(x)
y1 = func1(x)
y2 = func2(x)

plt.subplot(311)                   #3行1列排布子图，该为第1个子图
plt.plot(x,y,'r-')
plt.title('polynomial')

plt.subplot(312)                   #3行1列排布子图，该为第2个子图
plt.plot(x,y1,'b*')
plt.title('first derivative')

plt.subplot(313)                   #3行1列排布子图，该为第3个子图
plt.plot(x,y2,'go')
plt.title('sconde derivative')

plt.show()






