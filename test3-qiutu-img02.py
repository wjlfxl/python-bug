import requests
import re
import os

# os模块创建文件夹
if not os.path.exists('./imagesfile02'):
    os.mkdir('./imagesfile02')

url = 'https://www.qiushibaike.com/imgrank/page/%d/'

# UA伪装
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 '
}

# <div class="thumb">
#
# <a href="/article/124402104" target="_blank"> <img
# src="//pic.qiushibaike.com/system/pictures/12440/124402104/medium/HA8OH8EL1093N8EA.jpg" alt="糗事#124402104"
# class="illustration" width="100%" height="auto"> </a> </div>
# 上段数据解析得ex

# 用聚焦爬虫对图片爬取
# 解析放图片的标签
ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'

page_num = int(input("要爬多少页："))
new_url = format(url % page_num)

# 通用爬虫先对整个页面爬取
# content是二进制，
page_data = requests.get(url=new_url, headers=header).text

ex_data_list = re.findall(ex, page_data, re.S)
for src in ex_data_list:
    # 拼接
    src = 'https:' + src
    # URL=src 得到图片的地址
    img_data = requests.get(url=src, headers=header).content
    # split() 通过指定分隔符对字符串进行切片，如果参数num 有指定值，则分隔num + 1个子字符串
    # str.split(str="", num=string.count(str)).
    # 参数
    # str - - 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
    # num - - 分割次数。默认为 - 1, 即分隔所有。
    img_name = src.split('/')[-1]
    img_path = './imagesfile02/' + img_name
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
    print(img_name, "over")


