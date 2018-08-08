# -*- coding:utf-8 -*-
# Python version 3.6


# 1.分析LOL官网行为!
# 发现这个网页的所有数据都是经过js生成的!意思就是说 他的数据全部不在该网页里面,而是在一个JS文件里面!
# 所以我们只需要获取JS数据.


"""
抓取步骤及思路:


1.获取英雄的js数据,访问并且下载.然后转换为JSON格式的数据.


2.对数据进行解析,我们这边的函数式get_hero_data!
这个函数会对下载的json数据进行解析,提取出LOL中的英雄英文名字和id值!


3.访问并且下载:
    对于获取的数据进行拼接,尤其是对图片的链接进行拼接.然后进行下载!

"""

import requests
import json, re, os


class LOL_Spider(object):
    def __init__(self, url):
        self.url = url
    
    def get_hero_data(self):
        response = requests.get(self.url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36"},
                                timeout=10)
        if response.status_code == 200:
            with open("hero_data.json", "w")as f:
                f.write(json.dumps(response.text, indent=2))
        
        # 打开文件
        with open("hero_data.json", "r")as f:
            string = f.read()
        data = json.loads(string)
        
        hero_name = []  # 英雄的名字
        hero_id = []  # 英雄的图片id
        pattern1 = re.compile('"keys":{(.*?)},"data".*?')
        # 匹配出第一段数据!
        first_data = re.findall(pattern1, data)[0]
        pattern2 = re.compile('"(.*?)":"(.*?)"')
        for i in re.findall(pattern2, first_data):
            hero_id.append(i[0])  # id
            hero_name.append(i[1])  # 名字
        print(hero_name, "\n", hero_id)
        return hero_name, hero_id
    
    def download_pic(self, hero_name, hero_id):
        path = r'E:/LOLpic/'
        i = 0
        while i < len(hero_id):
            j = 0
            while j < 15:
                url = "http://ossweb-img.qq.com/images/lol/web201310/skin/big" + hero_id[i] + "00" + str(j) + ".jpg"
                # print(url)
                print("下载链接是:", url)
                response = requests.get(url, headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36"},
                                        timeout=10)
                if "404 page not found" in response.text:
                    print(hero_name[i], "下的皮肤已经下载完毕!!")
                    break
                else:
                    try:
                        os.mkdir(path + hero_name[i])
                    except FileExistsError:
                        pass
                    with open(path + hero_name[i] + "/" + str(j) + ".jpg", "wb")as f:
                        f.write(response.content)
                j += 1
            i += 1
    
    def Start_Spider(self):
        hero_name, hero_id = self.get_hero_data()
        self.download_pic(hero_name, hero_id)


if __name__ == "__main__":
    url = "http://lol.qq.com/biz/hero/champion.js"
    lol = LOL_Spider(url)
    lol.Start_Spider()
