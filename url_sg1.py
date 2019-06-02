from bs4 import BeautifulSoup as bs;
from urllib.request import urlopen
import re


sg   = "https://bbs.sgamer.com/forum-283-1.html"
resp = urlopen(sg).read().decode()
soup = bs(resp, "html.parser")
# all_data = soup.find_all(id="threadlisttableid")
# all_data = soup.find("table", {"id":"threadlisttableid"})
all_data = soup.select("tbody")

for normal in all_data:
    # soup_title = normal.find(class_="")
    soup_title  = normal.select(".xst")
    soup_author = normal.select(".by > cite > a")
    soup_say = normal.select(".num > a")
    soup_see = normal.select(".num > em")
    if soup_title:
        # print(soup_title[0].text)
        # print(soup_author[0].text)
        print(soup_author[1].text)  #最新回复
        # print(soup_say[0].text)
        # print(soup_see[0].text)

# print(all_data)
