__author__ = 'andrewliu'

import re
import requests
import time
import sys
from bs4 import BeautifulSoup

# date = time.strftime('[%Y-%m-%d]', time.localtime(time.time()))
# f_handle = open('out.log', 'w')
# sys.stdout = f_handle
# page = open('page.txt', 'r')
# content = page.readline()
# start_page = int(content.strip()) - 1
# page.close()

url = 'https://movie.douban.com/tag/top100?type=S'
# url = "http://www.webopedia.com/quick_ref/textmessageabbreviations.asp"
# Query_URL = 'https://frodo.douban.com/jsonp/subject_collection/movie_showing/items'
response = requests.get(url)
soup = BeautifulSoup(response.text)
# tag = soup.body.div
body = soup.find_all('div', class_='pl2')
# for item_title_ in body:
#     item_title = item_title_.find_all('a')
    # for item_a in title_:
    #     title = item_title.get_text()
    #     print(title)
# for item_profile_ in body:
#     item_profile = item_profile_.find_all('p')
#     for profiles in item_profile:
#         profile = profiles.get_text()
#         print(profile)

# for items_judges_ in body:
#     items_judges = items_judges_.find('div', class_='star clearfix').find('span', class_='rating_nums').get_text()
#     print(items_judges)

# images = soup.find_all('a', class_='nbg')
# for images_items in images:
#     print(images_items.find('img')['alt'])
#     print(images_items.find('img')['src'])
    # for image_item in images_items:
    #     title = image_item['title']
    #     print(title)

max_page = soup.find('span', class_='thispage')['data-total-page']