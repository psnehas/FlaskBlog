from flask import Flask,render_template,url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5429f57bf5529f17c206459d29daef8c'
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