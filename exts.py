# coding:utf-8
# /usr/bin/python

# creator = wangkai
# creation time = 2018/3/29 21:35

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
