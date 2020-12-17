
import os

# __name__ = "__init__.py"
# os.path.dirname("__init__.py") --> app/
# os.path.abspath("app") --> "/home/eyal/documents/di/python-bootcamp/class_11/di_site/app"

class Config:

    def __init__(self):
        self.basedir = os.path.abspath(os.path.dirname(__name__))

        self.UPLOAD_FOLDER = os.path.join(self.basedir, "app/uploads")

        self.SECRET_KEY = "chocolate"
        self.SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(self.basedir, "di_site.db")


conf = Config()
