#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微博爬虫配置模块
所有Headers配置或者代理IP都在该模块配置

@author: guoweikuang
"""
import os
import random


abs_path = os.path.abspath(os.path.dirname(__file__))
USER_AGENT = [
    'Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
    'Microsoft Internet Explorer/4.0b1 (Windows 95)',
    'Opera/8.00 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
    'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
]


def get_random_cookie():
    """ 随机获取cookie """
    path_from_cookies = os.path.join(abs_path, 'cookies')
    cookies = []
    for file in os.listdir(path_from_cookies):
        cookies.append(file)
    path = random.choice(cookies)
    cookie = open(path_from_cookies + '/' + path, 'rb').read().decode('utf-8')
    return cookie





