# -*- coding: utf-8 -*-
import redis

r = redis.Redis(host='ignore.com', port=6379,db=0)
r.set('name', 'zhangsan')   #添加
print (r.get('name'))   #获取