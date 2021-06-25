import requests
from lxml import etree
import os

if not os.path.exists('./imagesfile'):
    os.mkdir('./imagesfile')

url = 'https://pic.netbian.com/4kdongman/'

# UA伪装
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}

page_data = requests.get(url=url, headers=header)
# 处理乱码
page_data.encoding = page_data.apparent_encoding
page_data = page_data.text
# page_data.encoding = 'utf-8'

parser = etree.HTMLParser(encoding='utf-8')
tree = etree.HTML(page_data, parser=parser)

# xpath( 'xpath表达式')
# /表示从根节点开始，/表示一个层级,//是多个层级
# r = tree.xpath('/html/body/div')
# r = tree.xpath('//div')

# 属性定位 在标签后加[]，括号内@属性=属性名
# r = tree.xpath('//div[@class="book_sort"]')

# 属性定位后再定位
# r = tree.xpath('//div[@id="scroll_number"]//li')

# 属性定位后再再定位，   索引是从1开始的
# r = tree.xpath('//div[@id="scroll_number"]//li[3]')

# --------------------------------------------------------------------------
# 定位之后再拿属性和文本

# 1.定位
# r = tree.xpath('//div[@id="scroll_number"]//li[3]')

# 2.拿文本，获得的是['3']，列表元素加[0]为文本
# r = tree.xpath('//div[@id="scroll_number"]//li[3]/text()')[0]

# 3.拿某个li标签下的其他标签用//拿文本
# r = tree.xpath('//div[@id="scroll_number"]//li[7]//text()')[0]

# 4.拿某个div标签下的所有文本,连带\r\n  一起打印
# r = tree.xpath('//div[@id="scroll_number"]//text()')

# ------------------------------------------------------------------
# 取属性值 @tagN

title_list = tree.xpath('//div[@class="slist"]/ul/li')

for li in title_list:
    img_src = 'https://pic.netbian.com' + li.xpath('./a/img/@src')[0]

    img_name = li.xpath('./a/img/@alt')[0] + '.jpg'

    img_data = requests.get(url=img_src, headers=header).content
    img_path = './imagesfile/' + img_name
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
        print(img_name, 'over')
