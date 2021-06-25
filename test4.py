import requests
from bs4 import BeautifulSoup

# 通用爬虫先对整个页面爬取
url = 'https://www.shicimingju.com/book/sanguoyanyi.html'

# UA伪装
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 '
}

page_data = requests.get(url=url, headers=header).text.encode('iso-8859-1')

# print(page_data)
# with open('./sanguo.txt', 'w', encoding='utf-8') as fp:
#     fp.write(page_data)
# print(page_data, "over")

# 解析

soup = BeautifulSoup(page_data, 'lxml')

li_list = soup.select('.book-mulu>ul>li')

fp = open('./sanguo.txt', 'w', encoding='utf-8')
for li in li_list:
    title = li.a.string
    new_url = 'https://www.shicimingju.com' + li.a['href']
    # URL=new_url 得到新的地址
    new_page_text = requests.get(url=new_url, headers=header).text.encode('iso-8859-1')
    # split() 通过指定分隔符对字符串进行切片，如果参数num 有指定值，则分隔num + 1个子字符串
    # str.split(str="", num=string.count(str)).
    # 参数
    # str - - 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
    # num - - 分割次数。默认为 - 1, 即分隔所有。
    # 解析章节内容
    new_soup = BeautifulSoup(new_page_text, 'lxml')
    page_div_text = new_soup.find('div', class_='chapter_content')
    # 保存每章内容
    div_text = page_div_text.text
    fp.write(title + ':' + div_text + '\n')
    print(title, "over")
