import random

import requests
from lxml import etree

url = "https://namemc.com/minecraft-skins/trending/daily"

grabPageNum = 0

# for i in range(0, grabPageNum):
#     print(1)

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
myHeaders = {
    "cookie": '_gid=GA1.2.926373758.1675693346; qcmn=YYFRobCkZUdIVU--97zIFWDN; dnsDisplayed=undefined; ccpaApplies=false; signedLspa=undefined; _sp_su=false; __gpi=UID=00000bb6b8af37b4:T=1675693614:RT=1675693614:S=ALNI_MYE05mnFT1cIN0INHiFRJ6GdoaW5g; ccpaUUID=a0b5cab6-27db-4cec-89ee-6a849974eba4; __qca=P0-587628654-1675693616926; _lr_env_src_ats=false; _cc_id=a1f7434dcada56adb389bcc8e49de58e; panoramaId=df9ed3399022a68954b179118acea9fb927a66dc3013daa3d9de7be781e8e13b; panoramaId_expiry=1675780028866; pbjs-unifiedid_last=Mon%2C%2006%20Feb%202023%2014%3A39%3A29%20GMT; cto_bidid=VnUCqF9WZiUyQmNzdVkxOWw3eTZydzRWTFhqOVglMkJxcHl2TTFCS2tGRmZJa0E3RDdHY0oxY1VFdE5XdTA3QyUyRjBFaXlEM2JITG1MSlRWJTJGY251elhnV0huY0JZOXFrdkVqUFglMkYlMkZjb2lEcFVpQ3NmaFpIcyUzRA; cf_clearance=iEqsqNtSnJb_RpJCmeMV_okqxc.4rQ4RW5V3hzv8fUY-1675694672-0-160; consentUUID=2b6be673-9309-4405-b11a-6efb78bd11c2_16; __gads=ID=bc39ea8adeceb09a-228f6ca192d90067:T=1675693614:S=ALNI_MZjzK0vIjRUNdLpwSKDtzGGPpmTYA; _lr_retry_request=true; geo-store-location={"countryCode":"GB","stateProvCode":"ENG","stateProv":"England","isEuMember":"false","version":"1.0"}; _pbjs_userid_consent_data=3524755945110770; pbjs-unifiedid=%7B%22TDID%22%3A%22ec087e7c-7f6c-416f-92c9-f1e6d51d872f%22%2C%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222023-02-06T14%3A38%3A18%22%7D; referrer=https://namemc.com/minecraft-skins/trending/monthly; _ga_WPG9MK80J6=GS1.1.1675693601.1.1.1675698841.0.0.0; _ga=GA1.2.1256712525.1675693344; __cf_bm=q_.GgAAww3zNteRz5TIxRXSYxI7ZXDT3BVF6e3IPksc-1675698843-0-AYhXV0LIVjQkBf53y5rJ5Ht15DEYRKdZvNEzfZ5Gf3ncCF6aQQj8Bi3sCWeU3TBMdFAjhxiDDu33UwOqS9/aX/FrHmc+T54YvAX5hhULS4tyEPTSG5xAZBhsGTb/+cOck5UX+4VPgrXQ2rsnTBy7H0hGGpkqlZnstZ6fj1BOHYoXzdqmrjXFIcLV5RwsDaZf4Q==; cto_bundle=0jZSk19EQVdHb2FCNEwlMkZuSWdLQlo3aXFSQUV4RGN2ZXJKdlRtVjBTNlJ4UXpUMFU1MyUyQlplVXBia2E5QkhLcEduSTZOSlNYTExodlBXR3NTQ01PNFNSV3RMNXJzSjJhYVQySjNBVTRjQUQ2SldkSTFiUDdWeEFrMEZ2enNYWEpMYmU1SnhlbEpBYVNwZ3lWNXk2UjZQSEhxOFlBJTNEJTNE',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78"
}
# print(headers)
respect = requests.get(url, headers=myHeaders)
print(respect.text)

html = etree.HTML(respect.text)

divs = html.xpath("/html/body/main/div[2]/div/div[@class='col-4 col-md-2']")
print(divs)
for div in divs:
    skinHref = div.xpath("./div/a/text()")
    print(skinHref)




