# coding:utf-8
#author:itcker

import urllib.request   #import导入模块
import xlwt
from bs4 import BeautifulSoup

file = open("url.txt","r")   #打开url.txt "r"为阅读模式下

url_xls = []   #创建空列表
title_xls = []

for urls in file:
	url = urllib.request.urlopen(urls)
	soup = BeautifulSoup(url,"html5lib")   #解析html
	titles = soup.title.text

	url_xls.append(urls)   #添加元素到列表中
	title_xls.append(titles)
	
	#print (urls,titles)

workbook = xlwt.Workbook(encoding='utf-8')   #创建工作簿
sheet = workbook.add_sheet('Sheet1',cell_overwrite_ok=True)   #创建sheet

head = ['url', 'title']   # 表头部信息
for row in range(0, len(head)):   #len列表长度
	sheet.write(0, row, head[row], xlwt.easyxf('font: bold on'))

for column1 in range(0, len(url_xls)):
	sheet.write(column1 + 1, 0, url_xls[column1])
	column1 = column1 + 1

for column2 in range(0, len(title_xls)):
	sheet.write(column2 + 1, 1, title_xls[column2])
	column2 = column2 + 1

workbook.save('urltitle_xls.xls')   # 生成结果，保存到xls中
