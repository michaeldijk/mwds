import os
from flask import (Flask, flash, render_template, 
                    redirect, request, session, url_for)
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
    return render_template("register.html")


# run app, with environment variables from env.py local, otherwise from settings in Heroku
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")),
            debug=True)
            # don't forget to change debug = false later onwards, when testing is complete