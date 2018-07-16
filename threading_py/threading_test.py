# -*- coding: utf-8 -*-

import time
import requests
import concurrent
from concurrent import futures
import pandas as pd
import threading
from multiprocessing import Pool


# 装饰容器 打印函数执行时间
def gettime(func):
    def warapper(*args,**kwargs):
        print('='*50)
        print(func.__name__, 'Start ...')
        starttime = time.time()
        func(*args)
        endtime = time.time()
        spengtime = endtime - starttime
        print(func.__name__,'End ...')
        print('Spend',spengtime,'s totally')
        print('='*50)
    return warapper

# 从文件取 n 个网址测试
def get_urls_from_file(n):
    df = pd.read_csv('TestUrl.csv')
    # print(df)
    urls = list(df['url'][:n])

    return urls


#请求并解析网页获取数据
def getData(url, retries=3):
    # print('正在下载：',url)
    headers = {}
    try:
        html  = requests.get(url,headers=headers)
        # print(html)

    except requests.exceptions.ConnectionError as e :
        # print('下载错误[ConnectionError]:',e)
        html = None

    if (html != None and 500 <= html.status_code < 600 and retries):
        retries -= 1
        # print("服务器重试中....")
        getData(url,retries)
        data = html.text
    else:
        data = None
    return data

urls = get_urls_from_file(100)

#串行
@gettime
def Mynormal():
    for url in urls:
        getData(url)



#进程池
@gettime
def MyprocessPool(num=10):
    pool = Pool(num)
    results = pool.map(getData,urls)
    pool.close()
    pool.join()
    return results


#多线程
@gettime
def Mymultithread(max_threads=10):
    #对 urls的处理
    def urls_process():
        while True:
            try:
                #从urls末尾抽出一个url
                url = getData,urls.pop()
            except IndexError:
                #url 爬去完毕  为空结束
                break
            data = getData(url,retries=3)

            '''
            这里是对网页数据的提取与储存操作
            '''

    threads = []

    #未达到 最大线程
    while int(len(threads)<max_threads) and len(urls):
        thread = threading.Thread(target=urls_process)
        # print('创建线程'，thread.getName())
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


#线程池
@gettime
def Myfutures(num_of_max_works=10):
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_of_max_works) as executor:
        executor.map(getData,urls)


if __name__ == '__main__':
    #串行
    Mynormal()

    # 进程池
    MyprocessPool(10)
    # 多线程
    Mymultithread(10)
    # 线程池
    Myfutures(10)











