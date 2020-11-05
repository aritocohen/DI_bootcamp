import flask_wtf
import wtforms as wtf

class SignupForm(flask_wtf.FlaskForm):
    name        =   wtf.StringField(label="Name: ")
    age         =   wtf.IntegerField(label="Age: ")
    password    =   wtf.PasswordField(label="Password: ")

    submit      =   wtf.SubmitField(label="Sign up")

class SigninForm(flask_wtf.FlaskForm):
    name        =   wtf.StringField(label="Name: ")
    password    =   wtf.PasswordField(label="Password: ")

    submit      =   wtf.SubmitField(label="Sign up")
