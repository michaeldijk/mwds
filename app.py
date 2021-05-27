import os
import re
from flask import (Flask, flash, render_template, 
                    redirect, request, session, url_for)
import flask
from flask.templating import render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash



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
@app.route("/")
@app.route("/get_stories") # stories route (goes to homepage)
def get_stories():
    stories = mongo.db.stories.find() # find stories db, and assign it to variable stories
    return render_template("stories.html", stories=stories) # use variable stories, and assign it to stories


# Register template route
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already is present in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # if existing user check comes back with username from db, 
        # then flash message to user, and open register again
        if existing_user:
            flash("Username is already present, please choose another one...")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
        
        session["user"] = request.form.get("username").lower()
        flash("Registration Succesful, welcome to the club!")
        return redirect(url_for("profile", username=session["user"]))
    
    return render_template("register.html")


# Login template route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username is present in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            # ensure the password matches from db and user's input
            if check_password_hash(
                existing_user["password"], request.form.get("password")): 
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username does not exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")

# profile template route
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session users username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# logout template route
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have succesfully been logged out!")
    session.pop("user")
    return redirect(url_for ("login"))


# run app, with environment variables from env.py local, otherwise from settings in Heroku
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")),
            debug=True)
            # don't forget to change debug = false later onwards, when testing is complete