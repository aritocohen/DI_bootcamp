import flask_wtf
import wtforms as wtf
from wtforms import validators as vld

class NewPostForm(flask_wtf.FlaskForm):

    body        = wtf.TextAreaField("Body: ", validators=[vld.DataRequired("Post can't be empty !")])

    submit      = wtf.SubmitField(label="Post")

class SignupForm(flask_wtf.FlaskForm):
    name                = wtf.StringField(label="Name: ", validators=[vld.DataRequired("Name can't be empty")])
    pic                 = wtf.FileField(label="Profile picture: ")
    age                 = wtf.IntegerField(label="Age: ", validators=[vld.DataRequired()])
    password            = wtf.PasswordField(label="Password: ", validators=[vld.DataRequired(),
                                                                            vld.length(5, 10, "Password needs to be between 5 and 10 characters")])
    confirm_password    = wtf.PasswordField(label="Password: ", validators=[vld.EqualTo("password", message="Password doesn't match")])

    submit      = wtf.SubmitField(label="Sign in")

class SigninForm(flask_wtf.FlaskForm):
    name        = wtf.StringField(label="Name: ")
    password    = wtf.PasswordField(label="Password: ")

    submit      = wtf.SubmitField(label="Sign up")

