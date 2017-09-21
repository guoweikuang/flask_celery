# -*- coding: utf-8 -*-
import os


abs_path = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'what the fuck ,guoweikuang'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    FLASK_MAIL_SUBJECT_PREFIX = '[Guoweikuang]'
    FLASK_MAIL_SENDER = '15602200534@163.com'
    FLASK_ADMIN = os.environ.get('FLASK_ADMIN') or '15602200534@163.com'

    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or '15602200534@163.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'gwk2014081029'
    
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(abs_path, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(abs_path, 'data-test.sqlite')


class ProductConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(abs_path, 'data.sqlite')
    

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductConfig,
    'default': DevelopmentConfig,
}