# UA伪装
# user-agent（请求头：载体的身份标识），
# 如果识别是一个浏览器的请求就能接收请求
# 如果识别是一个不正常的请求就可能请求失败

# 所以要进行UA伪装，伪装成浏览器

import requests as rq

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}
# 1.指定url
url = 'https://www.sogou.com/web'
# 处理URL参数,封装到字典
kw = input('enter a word:')
param = {
    'query': kw
}

# 2.发起请求,params携带参数,headers请求头（简单的反反爬）
response = rq.get(url=url, params=param, headers=headers)

# 3.获取响应数据,text返回的是字符串形式数据
page_txt = response.text

# 4.持久化存储
filename = kw + ".html"
with open(filename, 'w', encoding='UTF-8') as fp:
    fp.write(page_txt)
print(filename, "爬取结束")
