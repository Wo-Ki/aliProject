# coding:utf-8
# /usr/bin/python

# creator = wangkai
# creation time = 2018/4/1 10:40

from . import *


class newOrEdit(FlaskForm):
    title = StringField(label=u"标题", validators=[DataRequired(u"请输入标题"), Length(1, 20, message=u'标题不能超过20字')])
    content = TextAreaField(label=u"正文")
    image1 = FileField(label=u'第一张',
                       validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg', 'gif'], u'文件为jpg,png,jpeg,gif格式')
                                   ])
    image2 = FileField(label=u'第二张', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'], u'文件为jpg,png,jpeg,gif格式')])
    image3 = FileField(label=u'第三张', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'], u'文件为jpg,png,jpeg,gif格式')])
    image4 = FileField(label=u'第四张', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'], u'文件为jpg,png,jpeg,gif格式')])
    image5 = FileField(label=u'第五张', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'], u'文件为jpg,png,jpeg,gif格式')])
    price = StringField(label=u'价格', validators=[DataRequired(), Regexp('^[0-9]*.[0-9]*$', 0, u"价格必须为整数或者小数")])
    province = SelectField(label=u"省份", id="province_id", choices=[('teacher', 'Teacher'),
                                                                   ('doctor', 'Doctor'),
                                                                   ('engineer', 'Engineer'),
                                                                   ('lawyer', 'Lawyer')])
    city = SelectField(label=u"当前城市", id="city_id", choices=[('teacher', 'Teacher'),
                                                             ('doctor', 'Doctor'),
                                                             ('engineer', 'Engineer'),
                                                             ('lawyer', 'Lawyer')])
    submit = SubmitField(label=u"发布")
