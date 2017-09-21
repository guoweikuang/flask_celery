# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, url_for, request, current_app
from app.main import main
from app.main.forms import ShowDataForm

# from tasks.tasks import crawl, send
from app.email import send_email, send_email1


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/show_data', methods=['GET', 'POST'])
def show_data():
    form = ShowDataForm(request.form)
    if form.validate_on_submit():
        url = form.url.data
        page = form.page.data
        for i in range(1, page):
            crawl.apply_async(args=[url, page], queue="crawl")
        return redirect(url_for('.show_data'))
    return render_template('show_data.html', form=form)


@main.route('/mail', methods=['GET', 'POST'])
def mail():
    # send.apply_async(args=['6711814@qq.com', 'Hello, world', 'mail/new_user'], queue='send')
    send_email('673411814@qq.com', 'hello, world', 'mail/new_user')
    return render_template('send_email.html')


