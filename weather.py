__author__ = 'andrewliu'
import requests

url = 'http://api.map.baidu.com/telematics/v3/weather?location=wuhan%9E&output=JSON&ak=FK9mkfdQsloEngodbFl4FeY3'
# url = 'http://v.juhe.cn/weather/index?format=2&cityname=%E8%8B%8F%E5%B7%9E'
# url = 'https://frodo.douban.com/jsonp/subject_collection/movie_showing/items'
# apikey = {'ak':'pcwIdfRjxnFNfwMKKkldWPtR1IHcbDrB'}
apikey = {'key' : '6926311f515c274c472517d61b618006','output':'json', 'location':'wuhan'}
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64)"
                        " AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
resp = requests.get(url)
print(resp.url)
print(resp.json())

# url = "pcwIdfRjxnFNfwMKKkldWPtR1IHcbDrB"
