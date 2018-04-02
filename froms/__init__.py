# coding:utf-8
# /usr/bin/python

# creator = wangkai
# creation time = 2018/3/30 15:56

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, NumberRange
from flask_wtf.file import FileField, FileAllowed, FileRequired
