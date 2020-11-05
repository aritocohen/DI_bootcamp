import flask

# Create a controller
app = flask.Flask(__name__) #__name__ is an automatic variable containing the name of the file

users = {
    "Alice": {"name": "Alice Cohen", "age": 45, "hobbies": ['Coding', 'Cooking', 'Scubadiving']},
    "Rick": {"name": "Rick Sanchez", "age": 59, "hobbies": ['Coding', 'Create things', 'Eating']},
}


# Create views

# URL: www.facebook.com/profile/rick
# URI: /profile/rick


@app.route("/")
def index():
    return flask.render_template("index.html", my_title="My awesome app")


@app.route("/users-list")
def users_list():

    return flask.render_template("users_list.html", users=users )


@app.route("/profile/<name>") #any value passed at the place of <name> will be transfered to the name argument
def profile_page(name):
    name = name.title()
    user = users[name]

    return flask.render_template("profile_page.html", user=user )
    
    
# Run my server

app.run()