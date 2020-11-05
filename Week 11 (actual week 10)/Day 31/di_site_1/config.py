import os

class Config:
    def __init__(self):

        basedir = os.path.abspath(os.path.dirname(__name__))

        self.SECRET_KEY = "chocolate"

        self.SQLALCHEMY_DATABASE_URI = "sqlite:///di_site.db" + os.path.join(self.basedir, "di_site.db")

config = Config()