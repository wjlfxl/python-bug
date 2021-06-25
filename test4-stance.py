import requests
from bs4 import BeautifulSoup

# 通用爬虫先对整个页面爬取
url = 'https://www.ihuoyzw.com/xs/108/254056/'

# UA伪装
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 '
}

page_data = requests.get(url=url, headers=header).text
# print(page_data)
# 解析

soup = BeautifulSoup(page_data, 'lxml')

li_list = soup.select('.box_con>div>dl>dd')

fp = open('./bl.txt', 'w', encoding='utf-8')
for li in li_list:
    title = li.a.string
    # print(title)
    new_url = 'https://www.ihuoyzw.com' + li.a['href']
    # print(new_url)
    # for page in range(1, 3):
    #     new_new_url = format(new_url % page)
    #
    #     print(new_url)
    # URL=new_url 得到新的地址
    new_page_text = requests.get(url=new_url, headers=header).text.encode('iso-8859-1')
    # print(new_page_text)
    # 解析章节内容
    new_soup = BeautifulSoup(new_page_text, 'lxml')
    page_div_text = new_soup.find('div', id='content')
    # 保存每章内容
    div_text = page_div_text.text
    fp.write(title + ':' + div_text + '\n')
    print(title, "over")

