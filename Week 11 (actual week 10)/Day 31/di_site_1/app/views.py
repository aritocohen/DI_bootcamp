import flask

from . import app # . is aliased to

from . import models, forms

@app.route("/")
def index():


    return flask.render_template("index.html")

@app.route("/about-us")
def about_us():


    return flask.render_template("about_us.html")


@app.route("/sign-up")
def signup():
    form    =   forms.SignupForm()

    if form.validate_on_submit():
        # 1) the form has been submitted
        # 2) The form contains valid data
        username    =   form.name.data
        password    =   form.password.data
        age         =   form.age.data

        my_user =   models.User(name=username, password=password, age=age)
        my_user.save()

        flask.flash("User has been succesfully registered")

        return flask.redirect("/")

    else:
        flask.flash("Something went wrong")
        print("Forms errors:", form.errors)

    return flask.render_template("signup.html", form=form)










