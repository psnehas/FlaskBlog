from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5429f57bf5529f17c206459d29daef8c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app) #instantiates the database 
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #this login is the name of the function under route decorator
login_manager.login_message_category = 'info' #adds bootstrap info bar arounnd the login message

from flaskblog import routes #this import statement is written here after db initialization to avoid circular routes.