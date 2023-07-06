import os

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
jwt = JWTManager(app)
socketio = SocketIO(app, cors_allowed_origins='*')
from app.sockets.message_socket import MessageSocket
message_socket = MessageSocket('/message')
socketio.on_namespace(message_socket)
