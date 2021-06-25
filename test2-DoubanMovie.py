import json
import requests as rq

# UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.77 Safari/537.36 '
}

# 1.指定url
get_url = 'https://movie.douban.com/j/chart/top_list'
# 处理URL参数,封装到字典
start_num=input("从哪开始:")
limit_num=input("取出个数:")
param = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': start_num,  # 从哪开始
    'limit': limit_num  # 取出个数
}

# 2.发起请求,params携带参数,headers请求头（简单的反反爬）
response = rq.get(url=get_url, params=param, headers=headers)

# 3.获取响应数据,text返回的是字符串形式数据
list_data = response.json()

# 4.持久化存储
filename = "moviebang.json"

fp = open(filename, 'w', encoding='UTF-8')
json.dump(list_data, fp=fp, ensure_ascii=False)
print("over")
