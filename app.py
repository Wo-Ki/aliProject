# coding:utf-8
# /usr/bin/python

# creator = wangkai
# creation time = 2018/3/29 21:27 


from flask import Flask, render_template, redirect, flash, url_for, request, session, Response, send_from_directory
from flask_bootstrap import Bootstrap
import config
from PIL import Image, ImageDraw, ImageFont, ImageFilter
# import Image, ImageDraw, ImageFont, ImageFilter
import random
from models import UserTable, ProductionTable, CommentTable
from flask_login import login_user, logout_user, current_user, login_required
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from sqlalchemy import or_
import base64
import datetime
from exts import db, login_manager
from froms import userForm, productionForm
import base64
import os
from io import BytesIO
import requests
import json

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
bootstrap = Bootstrap(app)
login_manager.init_app(app)

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)


@app.route("/index")
@app.route('/')
def index():
    productions = ProductionTable.query.order_by("-create_time").all()
    return render_template("index.html", title=u"首页", productions=productions)


@app.route('/publish', methods=["POST", "GET"])
@app.route('/edit/<int:id>/<method>', methods=["POST", "GET"])
@login_required
def publish(id=-1, method="edit"):
    form = productionForm.newOrEdit()
    li = ["image1", "image2", "image3", "image4", "image5"]
    image_urls = []
    if id == -1:  # 新建
        production = ProductionTable(user_id=current_user.id)
    else:  # 编辑
        production = ProductionTable.query.get_or_404(id)

    ip = request.remote_addr
    url = "http://ip.taobao.com/service/getIpInfo.php?ip=" + ip  # 根据当前ip获取位置
    jsonData = json.loads(requests.get(url).text)

    if form.validate_on_submit():
        if method == "edit":
            for l in li:
                image_data = request.files.get(l)
                if image_data:
                    setattr(production, l, image_data.filename)
                    print "image_data.filename:", image_data.filename
            production.title = form.title.data
            production.content = form.content.data
            production.city = form.city.data
            production.province = form.province.data
            production.price = form.price.data
            try:
                db.session.add(production)
                db.session.commit()
                image_urls = []
                if os.path.exists(os.path.join(app.config["UPLOADED_PHOTOS_DEST"], str(production.id))):
                    os.removedirs(os.path.join(app.config["UPLOADED_PHOTOS_DEST"], str(production.id)))
                os.mkdir(os.path.join(app.config["UPLOADED_PHOTOS_DEST"], str(production.id)))
                for l in li:
                    image_data = request.files.get(l)
                    if image_data:
                        filename = photos.save(image_data, folder=str(production.id))
                        print "filename:",filename
                        image_urls.append(photos.url(filename))
                return redirect(url_for('.index'))
            except:
                db.session.rollback()
                flash(u"发布失败", category="error")

        elif method == "remove":
            pass
        else:
            print "method error"
    form.title.data = production.title
    form.content.data = production.content
    form.city.data = production.city
    form.province.data = production.province
    form.price.data = production.price
    # form.image1.data = Image.open(os.path.join(p, str(production.image1)))
    # form.image2.data = Image.open(os.path.join(p, str(production.image2)))
    # form.image3.data = Image.open(os.path.join(p, str(production.image3)))
    # form.image4.data = Image.open(os.path.join(p, str(production.image4)))
    # form.image5.data = Image.open(os.path.join(p, str(production.image5)))
    imagePath = os.path.join(app.config["UPLOADED_PHOTOS_DEST"], str(production.id))
    if id != -1:
        savedImgs = os.listdir(imagePath)
        for i in savedImgs:
            image_urls.append(photos.url(os.path.join(str(production.id), i)))
    print "image_urls:", image_urls
    return render_template("edit.html", form=form, images=image_urls)


@app.route('/UserData/images/<filename>')
def upload(filename):
    print "upload:", app.config['UPLOAD_FOLDER'], filename
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/detail/<int:id>', methods=["POST", "GET"])
def detail(id):
    pass


@app.route("/login", methods=["GET", "POST"])
def login():
    form = userForm.LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        verification_code = form.verification_code.data
        user = UserTable.query.filter(UserTable.email == email).first()
        print "user", user
        if 'code_text' in session and session["code_text"] != verification_code:
            print "code_text"
            flash(message=u"验证码错误", category="warning")
        elif user is None:
            flash(message=u"该用户不存在", category="error")
        elif not user.check_password(password):
            flash(message=u"密码错误", category='error')
        else:
            login_user(user)
            return redirect(url_for("index"))
    code_img = getAuthPicture()
    title = u"登录"
    return render_template("login.html", form=form, title=title, code_img=code_img)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = userForm.RegisterForm()
    title = u"注册"
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        authText = form.verification_code.data

        find = UserTable.query.filter(UserTable.email == email).first()
        if 'code_text' in session and session["code_text"] != authText:
            flash(u"验证码错误", category="warning")
            # code_img = getAuthPicture()
            # return redirect(url_for(".register", form=form, code_img=code_img, title=title))
        elif find:
            flash(message=u"邮箱已经被注册", category='warning')
            # code_img = getAuthPicture()
            # return redirect(url_for(".register", form=form, code_img=code_img, title=title))
        else:
            user = UserTable(email=email, username=username, password=password)
            try:
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('.login'))
            except:
                db.session.rollback()
                flash(u"注册失败", category="error")
                code_img = getAuthPicture()
                return redirect(url_for(".register", form=form, code_img=code_img, title=title))
    code_img = getAuthPicture()
    # session['code_text'] = code_text
    return render_template("register.html", form=form, code_img=code_img, title=title)


@app.route("/about")
def about():
    return "about"


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.errorhandler(404)
def page_not_found(_):
    return render_template("404.html"), 404


def getAuthPicture():
    width = 50 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    # 输出文字:
    strOut = ""
    for t in range(4):
        char = rndChar()
        strOut += char
        draw.text((50 * t + 10, 10), char, font=font, fill=rndColor2())
    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    f = BytesIO()
    image.save(f, "png")
    data = f.getvalue()
    print "strOut:", strOut
    session['code_text'] = strOut
    return data


@app.route("/codePicCreator", methods=["GET"])
def codePicCreator():
    img_code = getAuthPicture()
    return Response(img_code)


# 随机字母:
def rndChar():
    return chr(random.randint(48, 57))


# 随机颜色1:
def rndColor():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


# 随机颜色2:
def rndColor2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


@app.template_test("current_link")  # jinja2
def is_current_link(link):
    return link == request.path


@app.context_processor
def my_context_processor():
    return {'base64': base64}


if __name__ == '__main__':
    app.run(debug=True)
