import flask
import flask_sqlalchemy
import flask_migrate

import os

from config import Config

db = flask_sqlalchemy.SQLAlchemy()
migrate = flask_migrate.Migrate()

app = flask.Flask(__name__)

app.config.from_object(config)

db.init_app(app)
migrate.init_app(app, db)

from . import views, models