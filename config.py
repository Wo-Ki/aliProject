# coding:utf-8
# /usr/bin/python

# creator = wangkai
# creation time = 2018/3/29 21:35

import os

DEBUG = True
SECRET_KEY = os.urandom(24)

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'aliProjectDB'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
# WTF_CSRF_ENABLED = False
WTF_CSRF_SECRET_KEY = os.urandom(24)
SSL_DISABLE = False
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_RECORD_QUERIES = True

BABEL_DEFAULT_LOCALE = 'zh'

# UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), "userData")
# UPLOAD_FOLDER = os.path.abspath(os.path.dirname(__file__))
# UPLOAD_FOLDER = os.path.abspath(os.path.dirname(__file__)) + "UserData/images/"
# UPLOAD_FOLDER = os.getcwd()
UPLOADED_PHOTOS_DEST = os.path.join(os.path.abspath(os.path.dirname(__file__)), "uploads")
