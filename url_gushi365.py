from bs4 import BeautifulSoup as bs;
from urllib.request import urlopen
import urllib.request
import re
# excel库
import xlsxwriter
import datetime
import time

import os

if not os.path.isdir("gushi365"):
    os.makedirs("gushi365")

number = input("Pls input page-number：")

for i in range(2, int(number) + 1):
    gushi365 = "http://www.gushi365.com/shuiqiangushi/index_"+ str(i) +".html"
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    
    req  = urllib.request.Request(url=gushi365,headers=headers)
    page = urllib.request.urlopen(req)
    resp = page.read().decode()
    
    #resp = urlopen(gushi365).read().decode()
    soup       = bs(resp, "html.parser")
    all_data   = soup.select("article")

    # 初始化
    startTime1 = '睡前故事365-第'+ str(i) +'页-' + str(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()))
    # startTime1 = 'asd'
    workbook  = xlsxwriter.Workbook('C:/Users/user/Desktop/github/EzCrawler/gushi365/' + startTime1 + '.xlsx')  # 创建一个Excel文件
    worksheet = workbook.add_worksheet()  # 创建sheet
    headings  = ['标题', '发布时间', '浏览量']  # 设置表头

    title = [U'gushi365', U'抓取数据']  # 表格title
    worksheet.write_row('A1', headings)  # title 写入Excel
    data_title = []
    data_time  = []
    data_read  = []
    for normal in all_data:
        soup_title = normal.select(".entry-title > a")
        soup_time  = normal.select(".entry-meta > .date")
        soup_read  = normal.select(".entry-meta > .views")
        if soup_title:
            data_title.append(soup_title[0].text)
            data_time.append(soup_time[0].text)
            data_read.append(soup_read[0].text)
    # print(all_data)
    worksheet.write_column('A2', data_title)
    worksheet.write_column('B2', data_time)
    worksheet.write_column('C2', data_read)
    workbook.close()