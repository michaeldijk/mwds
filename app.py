import os
import re
from flask import (Flask, flash, render_template,
                   redirect, request, session, url_for)
import flask
from flask.templating import render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm, LoginForm


# if local env. import env.py, otherwise not
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


# Setup instance of PyMongo linking to Flask App
mongo = PyMongo(app)


# Default route (index/homepage)
# stories route (goes to homepage)
@app.route("/")
@app.route("/get_stories")  
def get_stories():
    # find stories db, and assign it to variable stories
    stories = mongo.db.stories.find()
    # Ed Bradley, CI lead, helped me find a solution to filtering user avatars against stories written.
    users = list(mongo.db.users.find())
    # use variable stories, and assign it to stories
    # user variable users, assign it to users, to find avatars from users
    return render_template("stories.html", stories=stories, users=users)


# New story template route
@app.route("/new_story", methods=["GET", "POST"])
def new_story():
    if request.method == "POST":
        story = {
            "username": session["user"],
            "language_name": request.form.get("language_name"),
            "story_title": request.form.get("story_title"),
            "story_description": request.form.get("story_description")
        }
        mongo.db.stories.insert_one(story)
        flash("Story succesfully submitted!!")
        return redirect(url_for("get_stories"))

    languages = mongo.db.languages.find().sort("language_name", 1)
    return render_template("new_story.html", languages=languages)


# Edit story template route - coming from profile page
@app.route("/edit_story/<story_id>", methods=["GET", "POST"])
def edit_story(story_id):
    # If form is submitted, then post the following values
    if request.method == "POST":
        submit = {
            "username": session["user"],
            "language_name": request.form.get("language_name"),
            "story_title": request.form.get("story_title"),
            "story_description": request.form.get("story_description")
        }
        mongo.db.stories.update({"_id": ObjectId(story_id)}, submit)
        flash("Story has succesfully been updated!")
        return redirect(url_for("profile", username=session["user"]))

    # if page is opened, find values, and post to form
    story = mongo.db.stories.find_one({"_id": ObjectId(story_id)})
    languages = mongo.db.languages.find().sort("language_name", 1)
    return render_template("edit_story.html", story=story, languages=languages)


# delete story template route - coming from profile page
@app.route("/delete_story/<story_id>")
def delete_story(story_id):
    mongo.db.stories.remove({"_id": ObjectId(story_id)})
    flash("Story succesfully removed from database!")
    return redirect(url_for("profile", username=session["user"]))


# Login template route
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # check if username is present in db
        existing_user = mongo.db.users.find_one(
            {"username": form.username.data.lower()})

        if existing_user:
            # ensure the password matches from db and user's input
            if check_password_hash(existing_user["password"],
                                   form.password.data):
                session["user"] = form.username.data.lower()
                flash("Welcome, {}".format(form.username.data))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username does not exist
            flash("Username does not exist, please register!")
            return redirect(url_for("login"))

    return render_template("login.html", form=form)


# Register template route
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # check if username is already present in db
        existing_user = mongo.db.users.find_one(
            {"username": form.username.data.lower()})
        # if existing user check comes back with username from db,
        # then flash message to user, and open register again
        if existing_user:
            flash("Username is already present, please choose another one...")
            return redirect(url_for("register"))

        register = {
            "username": form.username.data.lower(),
            "email_address": form.email_address.data.lower(),
            "about_me": form.about_me.data.lower() or "Edit profile, if you want to enter a small bio",
            "avatar": form.avatar.data.lower() or "https://cdn.pixabay.com/photo/2016/08/08/09/17/avatar-1577909_1280.png",
            "password": generate_password_hash(form.password.data),

        }
        mongo.db.users.insert_one(register)

        session["user"] = form.username.data.lower()
        flash("Registration Succesful, welcome to the club!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html", form=form)


# profile template route
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session users username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    avatar = mongo.db.users.find_one(
        {"username": session["user"]})["avatar"]
    about_me = mongo.db.users.find_one(
        {"username": session["user"]})["about_me"]

    if session["user"]:
        # Find stories written by user, and return to page
        stories_written = mongo.db.stories.find(
            {"username": session["user"]}).sort("_id", -1)
        return render_template("profile.html", stories_written=stories_written, username=username, about_me=about_me, avatar=avatar)

    return redirect(url_for("login"))


# profile edit template route
@app.route("/profile/<username>/edit")
def profile_edit(username):
    form = RegisterForm()
    # grab the session users username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    return render_template("profile_edit.html", username=username, form=form)



# logout template route
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have succesfully been logged out!")
    session.pop("user")
    return redirect(url_for("login"))


# run app, with environment variables from env.py local,
# otherwise from settings in Heroku
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # don't forget to change debug = false
            # later onwards, when testing is complete
            debug=True)
