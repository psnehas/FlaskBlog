from flask import render_template,url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskblog.models import User, Post
from flask_login import login_user,current_user,logout_user,login_required
import secrets
import os
from PIL import Image

posts = [
    {
        "author":"Sneha",
        "title":"Blog post 1",
        "content": "first post",
        "date_posted":"apr 20"

    },
    {
        "author":"Rashmi",
        "title":"Blog post 2",
        "content": "second post",
        "date_posted":"may 20"

    }
]

@app.route("/")
def home():
    return render_template("home.html", posts = posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register", methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_pw )
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created. You can now log in','success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form= form)

@app.route("/login", methods = ["GET","POST"])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.rememberme.data)
            next_page = request.args.get('next')

            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:    
            flash(f'Login unsuccessful! Please check email and password', 'danger')
    return render_template('login.html', title="Login", form= form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    pict_hex_name = secrets.token_hex(8)
    _, fext = os.path.splitext(form_picture.filename)
    pict_fn = pict_hex_name+fext
    picture_path = os.path.join(app.root_path, 'static/user_profile_pics', pict_fn)
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return pict_fn

@app.route("/account",methods = ["GET","POST"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.image_file = picture_file
        db.session.commit()
        flash(f'Your account is updated', 'success')
        return redirect(url_for('account'))
    elif request.method=='GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        def funcname(parameter_list):
            pass
    image_file= url_for('static', filename='user_profile_pics/'+current_user.image_file)
    return render_template('account.html', title="Account", image_file = image_file, form=form)