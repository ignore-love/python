# -*- coding: utf-8 -*-
import sklearn
from sklearn import preprocessing

enc  = preprocessing.OneHotEncoder()

enc_fit = ([0,0,3],[1,1,0],[0,2,1],[1,0,2])
#print(type(enc_fit))

array = enc.transform([[0,1,3]]).toarray

print(type(array))