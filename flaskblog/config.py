import os

class Config:
    # SECRET_KEY = '5429f57bf5529f17c206459d29daef8c'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USERNAME = 'a.test.flask@gmail.com'
    # MAIL_PASSWORD = 'testflask'
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')