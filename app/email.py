# -*- coding: utf-8 -*-
from __future__ import absolute_import
from flask_mail import Message
from flask import current_app, render_template
from app import mail, create_app
from tasks.celery import app as celery_app


@celery_app.task(serializer='json', name="send")
def send_async_email(guo):
    app = create_app('default')
    with app.app_context():
        msg = Message('[Guoweikuang]' + guo['subject'],
                    sender='15602200534@163.com', recipients=[guo['to']])
        msg.body = "welcome to guoweikuang"
        msg.html = "<h1>Guoweikuang</h1>"
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    
    # msg = Message(current_app.config['FLASK_MAIL_SUBJECT_PREFIX'] + subject,
    #             sender=current_app.config['FLASK_MAIL_SENDER'], recipients=[to])
    # msg.body = render_template(template + '.txt', **kwargs)
    # msg.html = render_template(template + '.html', **kwargs)
    guo = {}
    guo['subject'] = subject
    guo['to'] = to
    guo['body'] = render_template(template + '.txt', **kwargs)
    guo['html'] = render_template(template + '.html', **kwargs)
    send_async_email.apply_async(args=[guo], queue='send')


def send_email1(to, subject, template, **kwargs):
    app = create_app('default')
    with app.app_context():
        msg = Message('[Guoweikuang]' + subject,
                    sender='15602200534@163.com', recipients=[to])
        msg.body = u"欢迎加入"
        msg.html = u"<h1>欢迎加入Guoweikuang的网站</h1>"
        mail.send(msg)
