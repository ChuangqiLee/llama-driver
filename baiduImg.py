import requests
from lxml import etree
import re
import random

myUserAgent = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]


def getImgUrls(__keyword, num):
    __urllist = []
    pn = 0
    rn = 10
    for i in range(0, num):
        url = "https://image.baidu.com/search/acjson?tn=resultjson_com&word={keyword}&pn={pn}&rn={rn}".format(
            keyword=__keyword, pn=pn, rn=rn)
        headers = {
            "User-Agent": random.choice(myUserAgent)
        }
        resp = requests.get(url=url, headers=headers)
        pattern = re.compile('"hoverURL":"http.*?"')
        results = pattern.findall(resp.text)
        for r in results:
            __urllist.append(r[12:-1])
        pn += 10
    return __urllist


def downloadImg(__urlList, __path, __name):
    __nameSuffix = 0
    for __url in __urlList:
        try:
            __headers = {
                "User-Agent": random.choice(myUserAgent)
            }
            r = requests.get(__url, headers=__headers)
            __imgName = __name + str(__nameSuffix) + '.jpg'
            with open(__path + '/' + __imgName, 'wb') as f:
                f.write(r.content)
            print(__imgName, "download over")
            __nameSuffix += 1
        except Exception as errorInfo:
            print("an exception occur this moment", errorInfo)



# 根据搜索的关键词从百度图库下载图片
# saveFolder 选择一个文件夹来保存下载的图片
# imgName 下载图片时的命名前缀
# num*10 = 下载的图片数量
keyword = "带有真人的广告牌"
saveFolder = r"C:\Users\ASUS\Desktop\Drone autopilot\data setting\Object detection\spider\advertisement"
imgName = "Abido"
num = 100
if __name__ == '__main__':
    imgList = getImgUrls(keyword, num)
    downloadImg(imgList, saveFolder, imgName)
    print("Download over.")
