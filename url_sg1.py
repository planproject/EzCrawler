from bs4 import BeautifulSoup as bs;
from urllib.request import urlopen
import re
# excel库
import xlsxwriter
import datetime
import time



sg   = "https://bbs.sgamer.com/forum-283-1.html"
resp = urlopen(sg).read().decode()
soup = bs(resp, "html.parser")
all_data = soup.select("tbody")

#初始化
# startTime1 = 'SG-' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
startTime1 = 'asd'
workbook = xlsxwriter.Workbook('D:/'+ startTime1 +'.xlsx')  #创建一个Excel文件
worksheet = workbook.add_worksheet()               #创建一个sheet
headings = ['Number','testA','testB']     #设置表头

title = [U'SG',U'抓取数据']     #表格title
worksheet.write_row('A1',headings)  #title 写入Excel
for normal in all_data:
    soup_title  = normal.select(".xst")
    soup_author = normal.select(".by > cite > a")
    soup_say = normal.select(".num > a")
    soup_see = normal.select(".num > em")
    if soup_title:
        data_title = soup_title[0].text
        data_author = soup_author[0].text
        data_rec = soup_author[1].text

        worksheet.write_column('A2', data_title)
        worksheet.write_column('B2', data_author)
        worksheet.write_column('C2', data_rec)
        # print(soup_title[0].text) #标题
        # print(soup_author[0].text)    #作者
        # print(soup_author[1].text)  #最新回复
        # print(soup_say[0].text)   #回复量
        # print(soup_see[0].text)   #阅读量
# print(all_data)

workbook.close()