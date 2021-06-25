import requests
from lxml import etree

url = 'https://www.aqistudy.cn/historydata/'

# UA伪装
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}

page_data = requests.get(url=url, headers=header).text
# print(page_data)
parser = etree.HTMLParser(encoding='utf-8')
tree = etree.HTML(page_data, parser=parser)


city_list = tree.xpath('//div[@class="bottom"]/ul[@class="unstyled"]/div/li')
# print(city_list)

fp = open('./city.txt', 'w', encoding='utf-8')
for city_li in city_list:
    title_li_list = city_li.xpath('./a/text()')[0]
    # print(title_li_list)
    fp.write(title_li_list + '\n')


