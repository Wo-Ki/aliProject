# coding:utf-8
# /usr/bin/python

# creator = wangkai
# creation time = 2018/3/29 21:35

from exts import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from markdown import markdown
from PIL import Image
from os import path
from io import BytesIO

basepath = path.abspath(path.dirname(__file__))
img = Image.open(basepath + "/static/images/defaultHeadPic.png").resize((45, 45))
f = BytesIO()
img.save(f, "png")
imgData = f.getvalue()
img.close()


class UserTable(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    telephone = db.Column(db.String(20))
    qqNum = db.Column(db.String(50))
    headPic = db.Column(db.BLOB, default=imgData)
    sex = db.Column(db.Integer)
    birthday = db.Column(db.DateTime)
    signature = db.Column(db.Text)
    isComment = db.Column(db.Boolean, default=False)

    create_time = db.Column(db.DateTime, default=datetime.now)
    productions = db.relationship("ProductionTable", backref="user")
    comments = db.relationship("CommentTable", backref="user")

    def __init__(self, *args, **kwargs):
        self.username = kwargs.get("username")
        self.password = generate_password_hash(kwargs.get("password"))
        self.email = kwargs.get("email")
        self.telephone = kwargs.get("telephone")
        self.qqNum = kwargs.get("qqNum")
        self.headPic = kwargs.get("headPic")
        self.sex = kwargs.get('sex')
        self.birthday = kwargs.get("birthday")
        self.signature = kwargs.get("signature")
        self.isComment = kwargs.get("isComment")

    def check_password(self, raw_password):
        return check_password_hash(self.password, raw_password)


@login_manager.user_loader
def load_user(user_id):
    return UserTable.query.get(int(user_id))


class ProductionTable(db.Model):
    __tablename__ = 'production'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text)

    image1 = db.Column(db.BLOB, nullable=False)
    image2 = db.Column(db.BLOB)
    image3 = db.Column(db.BLOB)
    image4 = db.Column(db.BLOB)
    image5 = db.Column(db.BLOB)

    price = db.Column(db.Integer, nullable=False)
    province = db.Column(db.String(50))
    city = db.Column(db.String(50))
    viewNum = db.Column(db.Integer, default=0)
    commitNum = db.Column(db.Integer, default=0)

    create_time = db.Column(db.DateTime, default=datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship("CommentTable", backref="production")

    @staticmethod
    def on_body_changed(target, value, oldvalue, initiator):
        if value is None or (value is ''):
            target.body_html = ''
        else:
            target.body_html = markdown(value)


db.event.listen(ProductionTable.content, 'set', ProductionTable.on_body_changed)


class CommentTable(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isRead = db.Column(db.Boolean, default=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    production_id = db.Column(db.Integer, db.ForeignKey('production.id'))
