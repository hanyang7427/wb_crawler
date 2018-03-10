# coding=utf-8
import resvole
import requests
import re
import pickle
from selenium import webdriver
import time
import csv
L = []
cnt = 0
a = re.compile(r'<a target="_blank" href="([^jpg]*?)" usercard="id=\d*?">.*?</a>')
def get_users(d):
    return re.findall(a,d.page_source)
with open('users.plk','rb') as f:
    p = pickle.load(f)
    with open('all_comment.plk','wb') as f2:
        for i in p:
            print(i)
            cnt = cnt + 1
            print(cnt)
            driver = webdriver.Firefox()
            driver.get('https:'+i)
            time.sleep(13)

            # 将页面滚动条拖到底部
            js = "var q=document.documentElement.scrollTop=1000000"
            js2 = "document.getElementsByClassName('WB_cardmore S_txt1 S_line1 clearfix')[0].click()"
            driver.execute_script(js)
            time.sleep(5)
            driver.execute_script(js)
            time.sleep(5)
            driver.execute_script(js)
            time.sleep(5)
            while True:
                try:
                    driver.execute_script(js2)
                    time.sleep(5)
                    driver.execute_script(js)
                except:
                    break
            for j in get_users(driver):
                if j not in L:
                    L.append(j)
            driver.quit()
        pickle.dump(L,f2)


# -------------------------------------------------------

with open('all_comment.plk','rb') as f:
    p = pickle.load(f)

http_raw_request_file = 'person_raw_request'
params = resvole.resvole_http_raw(http_raw_request_file)
cnt = 0
a = re.compile('<spanclass="item_textW_fl">(.*?)</span>')
b = re.compile('^//weibo.com/(\d*)$')

with open('address.csv','w',encoding='utf-8',newline='') as f1:
    writer = csv.writer(f1)
    for i in p:
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