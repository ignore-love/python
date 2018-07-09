# -*- coding: utf-8 -*-
import sklearn
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# 加载数据
iris=load_iris()
iris.keys()


n_samples,n_features=iris.data.shape


print("Number of sample :",n_samples)

print("Number of features :",n_samples)

####
print(iris.data[0])

####
print(iris.data.shape)

####
print(iris.target.shape)

####
print(iris.target)


iris = datasets.load_iris()
x_index = 3
color = ["blue","red","green"]

for label,color in zip(range(len(iris.target_names)),color):
    plt.hist(iris.data[iris.target==label,x_index],
             label=iris.target_names[label],
             color=color)
plt.xlabel(iris.feature_names[x_index])
plt.legend(loc='upper right')
plt.show()
