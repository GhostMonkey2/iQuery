__author__ = 'andrewliu'
import requests
from bs4 import BeautifulSoup

url = 'http://blog.knownsec.com/Knownsec_RD_Checklist/v3.0.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
skilltree = soup.find("div", {"class":"basetext", "id":"base"})
print (skilltree)
