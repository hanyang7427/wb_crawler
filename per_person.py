from bs4 import BeautifulSoup
import pickle
from selenium import webdriver
import time
import resvole
import requests
import re
import csv
with open('all_comment.plk','rb') as f:
    p = pickle.load(f)

print(len(p))


http_raw_request_file = 'person_raw_request'
params = resvole.resvole_http_raw(http_raw_request_file)
cnt = 0
a = re.compile('<spanclass="item_textW_fl">(.*?)</span>')
b = re.compile('^//weibo.com/(\d*)$')

with open('address.csv','w',encoding='utf-8',newline='') as f1:
    writer = csv.writer(f1)
    for i in p[:10]:
        print(i)
        cnt = cnt + 1
        print(cnt)
        try:
            num = re.search(b, i).groups()[0]
        except:
            num = 0
        if num:
            result = requests.get('https://weibo.com/u/'+num,headers=params[2])
            result = result.content.decode('utf-8')
            result = result.replace('\\t', '').replace('\\r', '').replace('\\n', '').replace(' ', '').replace('\\', '')
            address = re.findall(a,result)
        else:
            result = requests.get('https:'+i, headers=params[2])
            result = result.content.decode('utf-8')
            result = result.replace('\\t', '').replace('\\r', '').replace('\\n', '').replace(' ', '').replace('\\', '')
            address = re.findall(a, result)
        writer.writerow([i,address])