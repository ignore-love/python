# -*- coding: utf-8 -*-
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


# 调入数据
iris = load_iris()

# sklearn对数据集的介绍
# print(iris.DESCR)

# 提取数据内容
iris_data = iris.data
feature_names = iris.feature_names
iris_target = iris.target

# 格式整理
iris_target.shape = (150,1)
iris_all = np.hstack((iris_data, iris_target))

# 转化DataFrame
iris_data_df = DataFrame(iris_data,columns=feature_names)
iris_target_df = DataFrame(iris_target,columns=['target'])
iris_data_all_df = DataFrame(iris_all,columns=feature_names+['target'])

# 数据预览
# print("默认前5行")
# print(iris_data_all_df.head(2))   #默认前5行
# print("默认后5行")
# print(iris_data_all_df.tail(2))   #默认后5行
# print("随机抽取")
# print(iris_data_all_df.sample(2))  #随机抽取
# print("大小")
# print(iris_data_all_df.shape)
# print("类型")
# print(iris_data_all_df.dtypes)
# print("多种信息")
# print(iris_data_all_df.info())

# 统计描述
# print(iris_data_all_df.describe())  #常见 统计量的描述


# 数据范围
# sns.boxplot(data=iris_data_all_df)
# plt.show()

# 总览
# plt.plot(iris_data_df)
# plt.legend(feature_names)
# plt.show()


# 提取部分数据 （提取花萼数据 做图）
# 为了便于观察做出部分数据图
# sepal
sepal_data_df = iris_data_df[['sepal length (cm)','sepal width (cm)']]
plt.plot(sepal_data_df)
plt.legend(['sepal length (cm)','sepal width (cm)'])
plt.title('sepal data')
# plt.show()

sns.pairplot(iris_data_all_df, vars=iris_data_all_df.columns[:4], hue='target', size=3, kind='reg')
plt.show()

