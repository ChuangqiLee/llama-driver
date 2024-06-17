import requests
from lxml import etree
import re

# 创建会话
session = requests.session()

keyword = "原神阿贝多"
url = f"https://image.baidu.com/search/index?tn=baiduimage&ie=utf-8&word={keyword}".format(keyword=keyword)

session = requests.Session()
headers = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}

resp = session.get(url=url, headers=headers)

# 获取当前的Cookie
Cookie = dict(session.cookies)
print(Cookie)
print('=' * 60)
Cookie = str(Cookie)
Cookie = Cookie.replace("{'", "").replace("'}", "").replace("': '", "=").replace("', '", "; ")

headers['Cookie'] = Cookie
resp = session.get(url=url, headers=headers)
url = "https://image.baidu.com/search/acjson?tn=resultjson_com&word={keyword}&pn={pn}&rn={rn}".format(keyword=keyword,
                                                                                                      pn=30, rn=3)
# print(resp.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(resp.text)[0]))
print('=' * 60)
print(resp)

pattern = re.compile('hoverURL":".*?')
results = pattern.findall(resp)
html = etree.HTML(resp.text)

url = "https://image.baidu.com/search/acjson?tn=resultjson_com&word={keyword}&pn={pn}&rn={rn}".format(keyword=keyword,
                                                                                                      pn=30, rn=3)
