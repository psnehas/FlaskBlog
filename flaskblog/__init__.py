from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '5429f57bf5529f17c206459d29daef8c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app) #instantiates the database 

from flaskblog import routes #this import statement is written here after db initialization to avoid circular routes.