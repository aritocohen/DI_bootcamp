##################
###            ###
### MODELS.py  ###
###            ###
##################
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import flask_login
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import date

from . import db

class User(db.Model, UserMixin):

    id               = db.Column(db.Integer, primary_key=True)

    name             = db.Column(db.String(100))
    profile_pic_path = db.Column(db.String(500))
    age              = db.Column(db.Integer)
    password_hash    = db.Column(db.String(150))

    posts = db.relationship("Post", backref="author") # Every post where post.id == self.id

    @hybrid_property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, pwd):
        self.password_hash = generate_password_hash(pwd)

    def check_password(self, pwd):
        return check_password_hash(self.password_hash, pwd)

    @classmethod
    def login(cls, name, password):
        user = cls.query.filter_by(name=name).first_or_404()
        if user.check_password(password):
            flask_login.login_user(user)
            return True

        return False

    def add_post(self, post):
        # 1st way
        post.author = self
        # 2nd way
        self.posts.append(post)
        # 3rd way (not comfortable)
        post.user_id = self.id

        db.session.add(post)
        db.session.commit()

    def save(self):
        db.session.add(self)

        try:
            db.session.commit()
        except Exception as e: # If the try failed
            db.session.rollback()
            print(f"Error saving user {self.name}:", str(e))
        else: #    def email(self, email):
            print(f"Created user {self.name}")

    def __str__(self):
        return f"{self.name}"


class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    body        = db.Column(db.String(144))
    created_at  = db.Column(db.Date, default=date.today) #Don't execute date.today

    user_id     = db.Column(db.Integer, db.ForeignKey("user.id")) # SQL SIDE



