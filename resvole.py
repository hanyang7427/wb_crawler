import requests
from urllib.parse import urlparse
from urllib.parse import parse_qs
import re

# params_query ：    url内的参数
# params_body ：     post请求的data
# parmas_headers ：  http 的 headers
def resvole_http_raw(http_raw_req_file):
    re_header = re.compile(r'^([A-Z].*?): (.*)$')
    L = []
    def url2dict(url):
        query = urlparse(url).query
        return dict([(k, v[0]) for k, v in parse_qs(query).items()])
    with open(http_raw_req_file, 'r') as f:
        for line in f:
            L.append(line.strip())
    params_query = url2dict(L[0].split(' ')[1])
    params_body = dict([(k, v[0]) for k, v in parse_qs(L[-1]).items()])
    headers = []
    for header in L[1:-1]:
        if header:
            header = re.search(re_header, header).groups()
            headers.append(header)
    parmas_headers = dict(headers)
    return (params_query,params_body,parmas_headers)


def send_post_request(url, headers, data, params):
    content = requests.post(url, headers=headers, data=data, params=params).json()
    return content


def send_get_request(url, headers, params):
    content = requests.get(url, headers=headers, params=params).json()
    return content

