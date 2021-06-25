# xpath解析:最常用且最便捷高效的一种解析方式。通用性。
# -xpath解析原理:
# -1.实例化一个etree的对象，且需要将被解析的页面源码数据加载到该对象中。
# -2.调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的捕获。一环境的安装:
# -pip install lxml
# -如何实例化一个etree对象:from lxml import etree
# -1.将本地的html文档中的源码数据加载到etree对象中:
# etree.parse(filePath)
# -2.可以将从互联网上获取的源码数据加载到该对象中
# etree.HTML( 'page_text')
# xpath( 'xpath表达式')

from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')
tree = etree.parse('index.html', parser=parser)

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
# 取属性值 @tagName
# r = tree.xpath('//div[@class="scroll_mid"]/img/@src')


# print(r)
