# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, url_for, request
from flask_script import Manager, Shell
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_mail import Mail
from config import config
from flask_admin.contrib.sqla import ModelView


bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
flask_admin = Admin(name='Guoweikuang', template_mode="bootstrap3")

from app.models import User
flask_admin.add_view(ModelView(User, db.session))



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    flask_admin.init_app(app)
    # flask_admin.init_app(app)
    # from app.models import User
    # flask_admin.add_view(ModelView(User, db.session))

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


