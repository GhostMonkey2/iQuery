__author__ = 'andrewliu'

import re
import requests
import textwrap
from bs4 import BeautifulSoup
from prettytable import PrettyTable
# from .utils import colored, requests_get, exit_after_echo
# -*- coding: utf-8 -*-

"""
iquery.movies
~~~~~~~~~~~~~~
Movies query and display. The datas come
from:
    m.douban.com/movie
"""

class MoviesCollection:
    header = '编号 电影名称+上映日期 导演+主演+类型 豆瓣评分'.split()
    def __init__(self, rows):
        self._rows = rows

    def __len__(self):
        return len(self._rows)

    def movies(self):
        for idx, row in enumerate(self._rows):
            rating = row.get('rating')
            score = '{:.1f}'.format(rating.get('value')) if rating else '暂无'
            infos = row['info'].split('/')
            if re.match('\d', infos[-1]):
                time = infos[-1:]
                infos = '/'.join(infos[:-2])
            m = [
                idx + 1,
                '\n'.join([
                    row['title'],
                    time[0][:10],
                ]),
                infos,
                score
            ]
            yield m

    def _get_movie_summary(self, num):
        url = self._rows[num - 1].get('url')
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        s = re.sub(r'\s+', '', soup.find(property="v:summary").text)
        print(textwrap.fill(s, 40, initial_indent=''))


    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.header)
        for m in self.movies:
            pt.add_row(m)
        print(pt)

def query():

    Query_URL = 'https://frodo.douban.com/jsonp/subject_collection/movie_showing/items'
    response = requests.get(Query_URL)
    try:
        rows = response.json()['subject_collect_items']
    except (IndexError, TypeError):
        rows = []

    return MoviesCollection(rows)

