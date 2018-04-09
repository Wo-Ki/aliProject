# coding:utf-8
# /usr/bin/python

from . import *


class LoginForm(FlaskForm):
    email = StringField(label=u"邮箱:", validators=[DataRequired(), Email()])
    password = PasswordField(label=u"密码:", validators=[DataRequired()])
    verification_code = StringField(u'验证码:', validators=[DataRequired(), Length(4, 4, message=u'填写4位验证码')])
    submit = SubmitField(label=u"登录")


class RegisterForm(FlaskForm):
    username = StringField(label=u"用户名:", validators=[DataRequired(), Length(1, 50, message=u'用户长度为1到50'),
                                                     Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, u"用户名必须由数字，字母，下划线或者.组成")])
    email = StringField(label=u"邮箱:", validators=[DataRequired(), Email()])
    password = PasswordField(u"密码:", validators=[DataRequired(), Length(1, 6, message=u'填写1到6位密码'),
                                                EqualTo('password1', message=u"密码必须相同")])

    password1 = PasswordField(u"确定密码:", validators=[DataRequired()])
    verification_code = StringField(u'验证码:', validators=[DataRequired(), Length(4, 4, message=u'填写4位验证码')])
    submit = SubmitField(label=u"注册")
