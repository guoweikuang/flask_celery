# -*- coding: utf-8 -*-
from __future__ import absolute_import
from tasks.celery import app
from weibo_crawl.weibo import Weibo
from app.email import send_email


@app.task(name="crawl")
def crawl(url, page=1):
    weibo = Weibo(url, page)
    response = weibo.crawl()
    weibo.get_comment_num()


# @app.task(name="send")
# def send(to, subject, template, **kwargs):
#     send_email(to, subject, template, **kwargs)


