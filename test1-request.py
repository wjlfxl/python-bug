import requests as rq

# urllib 是一个老的、类似requests库的
# requests 是模仿浏览器发请求

# 流程：
# 1.指定url
url = "https://www.sogou.com/"
# url = "https://www.baidu.com/" 有乱码
# url = "http://scxk.nmpa.gov.cn:81/xk/"
# 2.发起请求
response = rq.get(url=url)
# 3.获取响应数据,text返回的是字符串形式数据
page_txt = response.text
print(page_txt)
# 4.持久化存储
with open('./sogou.html', 'w', encoding='UTF-8') as fp:
    fp.write(page_txt)
print("爬取结束")
