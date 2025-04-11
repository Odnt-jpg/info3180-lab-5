from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
# import flask migrate here
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models
from app import views
