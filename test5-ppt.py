import requests
from lxml import etree
import os

if not os.path.exists('./pptfile01'):
    os.mkdir('./pptfile01')

url = 'https://sc.chinaz.com/ppt/free.html'

# UA伪装
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.77 Safari/537.36 '
}

page_data = requests.get(url=url, headers=header)
# 处理乱码
page_data.encoding = page_data.apparent_encoding
page_data = page_data.text

# print(page_data)
parser = etree.HTMLParser(encoding='utf-8')
tree = etree.HTML(page_data, parser=parser)


ppt_page_list = tree.xpath('//div//div[@class="bot-div"]')
# print(ppt_page_list)
for ppt_list in ppt_page_list:
    ppt_src = 'https://sc.chinaz.com' + ppt_list.xpath('.//a/@href')[0]

    ppt_data = requests.get(url=ppt_src, headers=header)
    ppt_data.encoding = ppt_data.apparent_encoding
    new_page_data = ppt_data.text

    ppt_tree = etree.HTML(new_page_data, parser=parser)
    ppt_tree_list = ppt_tree.xpath('//div[@class="Free-download"]//div[@class="download-url"]')

    for new_ppt_list in ppt_tree_list:
        new_new_ppt_src = new_ppt_list.xpath('./a/@href')[0]

        new_ppt_data = requests.get(url=new_new_ppt_src, headers=header).url
        # split() 通过指定分隔符对字符串进行切片，如果参数num 有指定值，则分隔num + 1个子字符串
        # str.split(str="", num=string.count(str)).
        # 参数
        # str - - 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
        # num - - 分割次数。默认为 - 1, 即分隔所有。
        ppt_name = new_new_ppt_src.split('/')[-1]
        # print(ppt_name)
        new_ppt_path = './pptfile01/' + ppt_name + '.rar'
        with open(new_ppt_path, 'w') as fp:
            fp.write(new_ppt_data)
            print(new_new_ppt_src, 'over')



