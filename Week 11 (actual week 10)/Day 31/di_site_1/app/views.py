import time
import flask
import flask_login
from werkzeug.utils import secure_filename
import os

from . import app, db  # . is aliased to .__init__

from . import models, forms

@app.route("/")
def index():
    if flask_login.current_user.is_authenticated:
        # Build the url with the arguments
        url = flask.url_for('user_page', user_id=flask_login.current_user.id)
        return flask.redirect(url)

    return flask.render_template("index.html")

@app.route("/about-us")
def about_us():
    return flask.render_template("about_us.html")

@app.route("/users")
def users_list():
    # Retrieve users from the database (--> list of users)
    users = models.User.query.all()

    return flask.render_template("users_list.html", users=users)


@app.route("/user/<int:user_id>")
def user_page(user_id):
    # Retrieve the user
    user = models.User.query.get(user_id)
    if not user:
        return flask.redirect("/")

    return flask.render_template("user.html", user=user)


@app.route("/write-post", methods=["GET", "POST"])
@flask_login.login_required
def write_post():
    form = forms.NewPostForm()

    if form.validate_on_submit():
        # FORM HAS BEEN SUBMITTED
        # Use the results of the form to create a post
        post = models.Post(body=form.body.data)
        flask_login.current_user.add_post(post)

        flask.flash("Post has been written !")

        return flask.redirect("/")

    # Form hasn't been submitted

    return flask.render_template("write_post.html", form=form)


@app.route("/sign-up", methods=["GET", "POST"])
def signup():
    form = forms.SignupForm()

    if flask.request.method == "POST":
        if form.validate_on_submit():
            # 1) The form has been submitted
            # 2) The form contains valid data
            username = form.name.data
            password = form.password.data
            age      = int(form.age.data)

            picture = form.pic.data
            # Check extensions ? use os.path.splitext
            filename = secure_filename(picture.name + "-" + str(int(time.time())))

            path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            picture.save(path)

            my_user  = models.User(name=username, password=password, age=age, profile_pic_path=filename)
            my_user.save()

            flask.flash("User has been successfully registered", category="success")

            return flask.redirect("/")
        else:
            flask.flash("Something went wrong", category="danger")

    return flask.render_template("signup.html", form=form)

@app.route("/sign-in", methods=("GET", "POST"))
def signin():
    # Create a form object
    form = forms.SigninForm()

    # Test if the form has been submitted or not
    if form.valsend_from_directoryidate_on_submit():

        if models.User.login(form.name.data, form.password.data):
            flask.flash("User logged in successfully.", category="success")
            return flask.redirect("/")
        else:
            flask.flash("Something went wrong.", category="danger")


    return flask.render_template("signin.html", form=form)

@app.route("/sign-out")
def signout():
    flask_login.logout_user()

    return flask.redirect("/")


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return flask.send_from_directory(app.config["UPLOAD_FOLDER"], filename)
    # Same as
    # return flask.send_file(os.path.join(app.config["UPLOAD_FOLDER"], filename))

