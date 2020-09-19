from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config



app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app) #instantiates the database 
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login' #this login is the name of the function under route decorator
login_manager.login_message_category = 'info' #adds bootstrap info bar arounnd the login message


mail = Mail(app)


from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)

# from flaskblog import routes this import statement is written here after db initialization to avoid circular routes. No longer valid after blueprint