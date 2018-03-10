# coding=utf-8
import pickle
import resvole
from bs4 import BeautifulSoup
with open('mids.plk','rb') as f:
    d = pickle.load(f)

print(len(d))
print(d)

http_raw_request_file = 'http_raw_request.txt'
url = 'https://weibo.com/aj/v6/comment/small'


# 获取评论
def get_more_in_comment(mid):
    params = resvole.resvole_http_raw(http_raw_request_file)
    params[0]['mid']=mid
    more = resvole.send_get_request(url,params[2],params[0])
    return more
L = []
counter = 0
for i in d:
    print(i)
    counter = counter + 1
    print(counter)
    html = get_more_in_comment(i)['data']['html']
    soup = BeautifulSoup(html, 'lxml')
    link = soup.find('a',{'class':'WB_cardmore S_txt1 S_line1 clearfix'})
    print(11111)
    if not link:
        link = soup.find('a',{'class':'WB_cardmore WB_cardmore_v2 S_txt1 S_line1 clearfix'})
    L.append(link.get('href'))
with open('users.plk','wb') as f:
    pickle.dump(L,f)