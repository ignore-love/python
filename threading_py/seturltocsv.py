# -*- coding: utf-8 -*-
import re
import requests
import pandas as pd
from fake_useragent import UserAgent

url = 'https://www.hao123.com/'
ua = UserAgent()
headers = {'User-Agent':ua.random}

resp = requests.get(url,headers)
data = resp.text
urls = re.findall(r'href="(http.*?)"',data)
print(urls)

df = pd.DataFrame()

#取2000个
df['url'] = urls[:len(urls)]
df.to_csv('TestUrl.csv',index=None)

