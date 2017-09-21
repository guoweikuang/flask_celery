# -*- coding: utf-8 -*-
"""
数据库接口配置模块
"""
import pymysql
    

conn = pymysql.connect(host='localhost', 
                       user='root',
                       passwd='2014081029',
                       db='weibo',
                       charset='utf8')
db = conn.cursor()



def save_to_mysql(title, comments, likes, pub_time, url):
    try:
        sql = "INSERT new_content(微博内容, 发布时间, 评论个数, 点赞数, 微博内容链接) VALUES('%s', '%s', '%s', '%s', '%s')"
        sql = sql % (str(title.strip()), str(pub_time[:16]), str(comments), str(likes), str(url))

        # db.execute(sql, (title, str(pub_time[:16]), str(comments), str(likes), str(url)))
        db.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()



