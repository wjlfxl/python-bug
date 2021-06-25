import json
import requests as rq

# requests发起请求
# params参数是用来发送查询字符串，data是用来发送正文
# post两种方法都能用，get只能用params

# UA伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.77 Safari/537.36 '
}

# 1.指定url
get_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'

id_list = []  # 保存ID
# 处理URL参数,封装到字典
for page in range(1, 6):
    page = str(page)
    data = {
        'on': 'true',
        'page': page,
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applysn': ''
    }
    # 2.发起请求
    # 3.获取响应数据,json
    page_json = rq.post(url=get_url, data=data, headers=headers).json()
    # 过滤id
    for dic in page_json['list']:
        id_list.append(dic['ID'])

# 4.持久化存储
# fp = open('./father_scxk.json', 'w', encoding='UTF-8')
# json.dump(page_data, fp=fp, ensure_ascii=False)

# ------------------------------------------------------------
# 第二重页面
son_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
all_data_list = []
for id in id_list:
    son_param = {
        'id': id
    }
    # 2.发起请求
    # 3.获取响应数据,json
    # son_response = rq.post(url=son_url, params=son_param, headers=headers)
    # page_data = son_response.json() 两句结合为下面一句
    son_json = rq.post(url=son_url, params=son_param, headers=headers).json()
    print(son_json)
    all_data_list.append(son_json)

# 4.持久化存储
fp = open('./son_scxk.json', 'w', encoding='UTF-8')
json.dump(all_data_list, fp=fp, ensure_ascii=False)
