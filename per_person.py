# coding=utf-8
'''
    获取每个人所在城市
'''
import pickle
import resvole
import requests
import re
import csv
# all_comment.plk 所有的微博rul
# p为list
with open('all_comment.plk','rb') as f:
    p = pickle.load(f)

print(len(p))


http_raw_request_file = 'person_raw_request'
params = resvole.resvole_http_raw(http_raw_request_file)
cnt = 0
# 城市名称正则
a = re.compile('<spanclass="item_textW_fl">(.*?)</span>')
# id正则
b = re.compile('^//weibo.com/(\d*)$')

# 将微博id和所在城市写入csv
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