# coding:utf-8
# /usr/bin/python

# creator = wangkai
# creation time = 2018/3/29 21:35

from werkzeug.utils import secure_filename
from flask_script import Manager, Shell
from app import app
from flask_migrate import Migrate, MigrateCommand, upgrade
from exts import db
from models import UserTable, ProductionTable, CommentTable

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
