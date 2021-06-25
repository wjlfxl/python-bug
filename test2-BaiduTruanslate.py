import json
import requests as rq

# UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.77 Safari/537.36 '
}

# 1.指定url
post_url = 'https://fanyi.baidu.com/sug '
# 处理URL参数,封装到字典
word=input("enter a word:")
data = {
    'kw': word
}

# 2.发起请求,params携带参数,headers请求头（简单的反反爬）
response = rq.post(url=post_url, data=data, headers=headers)

# 3.获取响应数据,text返回的是字符串形式数据
dic_obj = response.json()

# 4.持久化存储
filename = word + ".json"

fp = open(filename, 'w', encoding='UTF-8')
json.dump(dic_obj, fp=fp, ensure_ascii=False)
