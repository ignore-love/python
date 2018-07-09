# -*- coding: utf-8 -*-
import requests
import pandas as pd
from bs4 import BeautifulSoup


# 请求数据
def get_data():
    url = 'https://book.douban.com/latest'
    # headers
    headers = {
        'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
    }
    data = requests.get(url,headers = headers)
    return  data

# 解析数据
def parse_data(data):

    bsObj = BeautifulSoup(data.text, 'lxml')
    # print(bsObj)
    book_left = bsObj.find('ul',{'class':'cover-col-4 clearfix'})
    book_left = book_left.find_all('li')
    book_right = bsObj.find('ul',{'class':'cover-col-4 pl20 clearfix'})
    book_right = book_right.find_all('li')

    books = list(book_left)+list(book_right)

    #对每一个图书 进行相同操作
    img_urls = []
    titles = []
    ratings = []
    authors = []
    details = []
    for book in books:
        # 图书封面
        img_url = book.find_all("a")[0].find('img').get("src")
        print("img_urls: ",  print("img_urls: ", img_urls))
        img_urls.append(img_url)
        #标题
        title = book.find_all('a')[1].get_text()
        print("titles: ", title)
        titles.append(title)
        #评价星级
        rating = book.find('p',{'class':'rating'}).get_text()
        rating = rating.replace('\n','').replace(' ','')
        print("ratings: ", rating)
        ratings.append(rating)
        # 作者
        author = book.find('p',{"class":"color-gray"}).get_text()
        author = author.replace('\n','').replace(' ','')
        print("authors: ", author)
        authors.append(author)
        # 简介
        detail = book.find_all('p')[2].get_text()
        detail = detail.replace('\n','').replace(' ','')
        details.append(detail)
        print("details: ", detail)

    return img_urls,titles,ratings,authors,details


# 储存数据
def save_data(img_urls,titles,ratings,authors,details):
    result = pd.DataFrame()
    result['img_urls'] =img_urls
    result['titles'] =titles
    result['ratings'] =ratings
    result['authors'] =authors
    result['details'] =details
    result.to_csv('d:/duobanbook.csv',index=None)

def run():
    data = get_data()
    img_urls, titles, ratings, authors, details = parse_data(data)
    # print(type(parse_data(data)))
    save_data(img_urls,titles,ratings,authors,details)


if __name__ == '__main__':
    run()

    # parse_data(get_data())