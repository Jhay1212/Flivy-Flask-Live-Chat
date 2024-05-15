from flask import Flask
from flask_socketio import SocketIO, join_room, leave_room, send
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)
socket = SocketIO(app)
app.app_context().push()