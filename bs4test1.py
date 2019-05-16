import requests
from bs4 import BeautifulSoup

# res = requests.get("http://heater.fsociaty.com")
# res.encoding = 'gbk'
# data = res.text
# print(data.encode('GBK', 'ignore'))

res = requests.get("https://www.douyu.com/g_DOTA2")
soup = BeautifulSoup(res.text)
for item in soup.select('.layout-Cover-item'):
    print(item.select('.DyListCover-intro')[0].text)
    print(item.select('.DyListCover-user')[0].text)
    print(item.select('.DyListCover-hot')[0].text)
