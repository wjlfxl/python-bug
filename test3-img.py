# 聚焦爬虫:爬取页面中指定的页面内容。
# 一编码流程:
# 1.一指定url
# 2.发起请求
# 3.获取响应数据一数据解析
# 4. 持久化存储


# 数据解析分类:
# -正则
# - bs4
# - xpath (水水*)

# 数据解析原理概述:
# 一解析的局部的文本内容都会在标签之间或者标签对应的属性中进行存储
# -1.进行指定标签的定位
# -2.标签或者标签对应的属性中存储的数据值进行提取（解析)
import requests
url = "http://www.xinhuanet.com/photo/2021-06/07/1127536917_16230298602581n.jpg"

# content是二进制，
img_data=requests.get(url=url).content
with open('./img.jpg','wb') as fp:
    fp.write(img_data)


