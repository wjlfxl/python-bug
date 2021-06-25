import requests
from lxml import etree

url = 'https://wh.58.com/ershoufang/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&PGTID=0d100000-0009-e505-4ae2-c77df91b8cfe&ClickID=2'

# UA伪装
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}

page_data = requests.get(url=url, headers=header).text

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

title_list = tree.xpath('//section//div[@class="property-content-title"]')
fp = open('./58.txt', 'w', encoding='utf-8')
for li in title_list:
    title_li_list = li.xpath('./h3/text()')[0]
    fp.write(title_li_list + '\n')
    print(title_li_list)
