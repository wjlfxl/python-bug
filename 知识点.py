import requests
# import re
# import os
from bs4 import BeautifulSoup
import lxml

# bs4进行数据解析
# 一数据解析的原理:
# -1.标签定位
# -2.提取标签、标签属性中存储的数据值
#
#
# - bs4数据解析的原理:
# -1.实例化一个BeautifulSoup对象，并且将页面源码数据加载到该对象中
# -2.通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取
#
# 一如何实例化BeautifulSoup对象;
# - from bs4 import BeautifulSoup一对象的实例化:
# -1-将本地的html文档中的数据加载到该对象中
# -2.将互联网上获取的页面源码加载到该对象中

# ---------------------------------------------------------------

# 1-将本地的html文档中的数据加载到该对象中
fp = open('index.html', 'r', encoding='utf-8')
soup = BeautifulSoup(fp, 'lxml')
# print(soup)

# ---------------------------------------------------------------
# -2.将互联网上获取的页面源码加载到该对象中
# page_text=response.text
# soup=(page_text'lxml')


# 属性:

# .tagName:返回首次出现的a标签
# find('tagName')与soup.a等同
# print(soup.a)
# print(soup.find('a'))
# print(soup.div)


# 属性定位
# find（）：class_ 可以定位到含class名的标签，也可以是id，attr
print(soup.find('div', class_='scroll_top'))

# find_all（）：class_ 可以定位到含class名的标签，也可以是id，attr，all所有
print(soup.find_all('div', class_='scroll_top'))

# -----------------------------------------------------
# soup.select('')

# 多层选择器
# soup.select( '.tang > ul > li > a')∶>表示的是一个层级
# 在class=tang下的ul下的li的所有a标签，然后所有a标签是第一个标签
print(soup.select('#book_focus >dd > a')[0])

# 空格表示多个层级
print(soup.select('#book_focus >dd a')[0])

# 隐去标签只留内容
# - text/get_text():可以获取某一个标签中所有的文本内容
# -string:只可以获取该标签下面直系的文本内容
# 隐去标签只留文本内容
print(soup.select('#book_focus >dd > a')[0].text)
print(soup.select('#book_focus >dd > a')[0].get_text())
print(soup.select('#book_focus >dd > a')[0].string)

# 获取第一个a标签的class属性的值
print(soup.select('#book_focus >dd > a')[0]['class'])

