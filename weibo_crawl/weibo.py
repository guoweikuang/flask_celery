#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微博爬虫主体，获取微博内容
"""
import re
import random
import requests
from bs4 import BeautifulSoup

from .settings import get_random_cookie, USER_AGENT
from .utils import get_logger, handle_time
from .db import save_to_mysql


logger = get_logger()


class Weibo(object):
    """微博主体"""
    def __init__(self, url, page=1):
        self.url = url
        self.page = page
        self.headers = {
            'User-Agent': random.choice(USER_AGENT),
            'Cookie': get_random_cookie()
        }
    def crawl(self):
        url = self.url + '?page={}&vt=4'.format(self.page)
        try:
            response = requests.get(url, headers=self.headers, timeout=5)
            if response.status_code == 200:
                return response.content
        except requests.exceptions.ConnectTimeout:
            logger.error('ConnectTimeout')
        except requests.exceptions.Timeout:
            logger.error('Timeout')
        except Exception as e:
            logger.error('UnKonwn: %s' % e)
        return None
    
    def get_comment_num(self):
        num_comment = []
        num_zan = []
        response = self.crawl()
        if not response:
            pass
        else:
            soup = BeautifulSoup(response, 'lxml')
            for items in soup.find_all('div', class_="c", id=True):
                total = items.find_all('a')[::-1]
                comments = str(total[1])
                num_comment = re.findall(r'\[(\d+)\]', comments)
                num_comment = int(num_comment[0])

                if num_comment > 0:
                    # 标题
                    title = items.find('span', class_="ctt").get_text()
                    title = title.replace('http://t.cn/Roeb5AN', '')
                    # 点赞数
                    like = str(total[3])
                    like = re.findall(r'\[(\d+)\]', like)
                    like = int(like[0])
                    # 发布时间
                    pub_time = items.find('span', class_="ct")
                    re_pattern = re.compile(u'[^\u0000-\uD7FF\uE000-\uFFFF]', re.UNICODE)
                    pub_time = pub_time.get_text().strip()
                    pub_time = re.sub(re_pattern, r'', pub_time)
                    pub_time = handle_time(pub_time)
                    # url链接，用来去重
                    url = items.find('a', class_="cc")
                    url = url.get('href')
                    print(num_comment, like, title,url)
                    save_to_mysql(title, num_comment, like, pub_time, url)
                    print(pub_time[:16])

           
if __name__ == '__main__':
    url = 'https://weibo.cn/gzyhl'
    weibo = Weibo(url, 1)
    response = weibo.crawl()
    weibo.get_comment_num()
    # print(response)