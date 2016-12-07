__author__ = 'andrewliu'
import requests
from bs4 import BeautifulSoup
import re

response = requests.get("http://en.wikipedia.org/wiki/Kevin_Bacon")
soup = BeautifulSoup(response.text)
links = soup.find('div',{'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)'))
for link in links:
    if 'href' in link.attrs:
        print(link['href'])



