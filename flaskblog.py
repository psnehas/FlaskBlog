from flask import Flask,render_template,url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '5429f57bf5529f17c206459d29daef8c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app) #instantiates the database 

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg') #will use a hashing technique that converts the image uri to a 20 characters long string
    password = db.Column(db.String(60),nullable=False) #will use a hashing technique that converts the password to a 60 characters long string
    posts = db.relationship('Post', backref='author',lazy=True)
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}','{self.date_posted}')"


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
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form= form)

@app.route("/login", methods = ["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You are now looged in!','success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful! Please check username and password', 'danger')
    return render_template('login.html', title="Login", form= form)

if __name__ == "__main__":
    app.run(debug=True)