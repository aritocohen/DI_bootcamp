import flask
import flask_sqlalchemy
import flask_migrate
import flask_login


from config import conf

db  = flask_sqlalchemy.SQLAlchemy()
migrate = flask_migrate.Migrate()
login_mgr = flask_login.LoginManager()

app = flask.Flask(__name__)

app.config.from_object(conf)

## AFTER APP CREATION
from . import views, models

db.init_app(app)
migrate.init_app(app, db)
login_mgr.init_app(app)

@login_mgr.user_loader
def load_user(user_id):
    return models.User.query.get(user_id)


