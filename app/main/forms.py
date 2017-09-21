# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class ShowDataForm(Form):
    url = StringField(u"抓取链接", validators=[DataRequired(
                    message=u"请输入抓取链接（https://weibo.cn/gzyhl)")])
    page = IntegerField(u"抓取页数", validators=[DataRequired()])
    submit = SubmitField(u"开始抓取")