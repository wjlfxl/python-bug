import json
import requests as rq

# 1.指定url
get_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
# 处理URL参数,封装到字典
keyword = input("输入关键字:")
param = {
    'cname': '',
    'pid': '',
    'keyword': keyword,
    'pageIndex': '1',
    'pageSize': '10'
}

# UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.77 Safari/537.36 '
}

# 2.发起请求,params携带参数,headers请求头（简单的反反爬）
response = rq.post(url=get_url, params=param, headers=headers)

# 3.获取响应数据,text返回的是字符串形式数据
page_text = response.text

# 4.持久化存储
filename = "NFC.txt"

with open(filename, 'w', encoding='UTF-8') as fp:
    fp.write(page_text)
print("over")
