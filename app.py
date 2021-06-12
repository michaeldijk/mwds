import os
import re
from dns.query import receive_udp
from flask import (Flask, flash, render_template,
                   redirect, request, session, url_for)
import flask
from flask.templating import render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm, LoginForm, EditProfileForm, ContactForm, NewStoryForm, EditStoryForm, EditLanguageForm, AddLanguageForm
from flask_paginate import Pagination, get_page_parameter
from flask_mail import Mail, Message
from datetime import datetime


# if local env. import env.py, otherwise not
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


# Setup instance of PyMongo linking to Flask App
mongo = PyMongo(app)

# Mail settings below
mail = Mail()

app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_SSL"] = os.environ.get("MAIL_USE_SSL")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
 
mail.init_app(app)

# Default route (index/homepage)
# stories route (goes to homepage)
@app.route("/")
@app.route("/get_stories")
def get_stories():

    page = int(request.args.get('page', 1))
    per_page = 10
    offset = (page - 1) * per_page

    search = False
    q = request.args.get("q")
    if q:
        search = True
    # Pagination from flask: https://pythonhosted.org/Flask-paginate/
    # Found solution to showing correct values from: 
    # https://stackoverflow.com/questions/54053873/implementation-of-pagination-using-flask-paginate-pymongo
    page = request.args.get(get_page_parameter(), type=int, default=1)
    # find stories db, and assign it to variable stories
    stories = mongo.db.stories.find()
    # filter stories, with pages, and assign it to all_stories
    all_stories = mongo.db.stories.find().sort("_id", -1).skip((page - 1) * per_page).limit(per_page)
    pagination = Pagination(page=page, total=stories.count(), search=search, record_name="stories", css_framework='bootstrap4')
    # Ed Bradley, CI lead, helped me find a solution to filtering user avatars against stories written.
    users = list(mongo.db.users.find())
    # use variable stories, and assign it to stories
    # user variable users, assign it to users, to find avatars from users
    return render_template("stories.html", stories=all_stories, users=users, pagination=pagination)

# single story route
@app.route("/single_story/<story_id>")
def single_story(story_id):
        if "user" in session:
            if session["user"]:
                users = list(mongo.db.users.find())
                story = mongo.db.stories.find_one({"_id": ObjectId(story_id)})
                return render_template("single_story.html", story=story, users=users)
        
        flash("Access denied. Create an account to view full stories", "error")
        flash("Or, login with your credentials below")
        return redirect(url_for("login"))


# New story template route
@app.route("/new_story", methods=["GET", "POST"])
def new_story():
        if "user" in session:
            if session["user"]:
                form = NewStoryForm()
                # Found help populating choices, from https://stackoverflow.com/questions/28133859/how-to-populate-wtform-select-field-using-mongokit-pymongo
                form.languages.choices = [(item["language_name"]) for item in mongo.db.languages.find().sort("language_name", 1)]
                if form.validate_on_submit():
                    story = {
                        "username": session["user"],
                        "language_name": form.languages.data,
                        "story_title": form.title.data.lower(),
                        "story_description": form.story.data,
                        "posted_date": str(datetime.today())
                    }
                    mongo.db.stories.insert_one(story)
                    flash("Story succesfully submitted!!")
                    return redirect(url_for("get_stories"))

                return render_template("new_story.html", form=form)
        
        flash("Access denied. Create an account to post new stories", "error")
        flash("Or, login with your credentials below")
        return redirect(url_for("login"))


# Edit story template route - coming from profile page
@app.route("/edit_story/<story_id>", methods=["GET", "POST"])
def edit_story(story_id):
        if "user" in session:
            story_username = mongo.db.stories.find_one({"_id": ObjectId(story_id)})["username"]
            if session["user"] == story_username:
                # Get values from database below
                story = mongo.db.stories.find_one({"_id": ObjectId(story_id)})
                language = mongo.db.stories.find_one({"_id": ObjectId(story_id)})["language_name"]
                story_title = mongo.db.stories.find_one({"_id": ObjectId(story_id)})["story_title"]
                story_description = mongo.db.stories.find_one({"_id": ObjectId(story_id)})["story_description"]
                languages = mongo.db.languages.find().sort("language_name", 1)
                # Form with values from above
                form = EditStoryForm(languages=language, title=story_title, story=story_description)
                # Populate languages from database in alphabetic order
                form.languages.choices = [(item["language_name"]) for item in mongo.db.languages.find().sort("language_name", 1)]
                
                if form.validate_on_submit():
                    story = {
                        "username": session["user"],
                        "language_name": form.languages.data,
                        "story_title": form.title.data,
                        "story_description": form.story.data
                    }
                    mongo.db.stories.update({"_id": ObjectId(story_id)}, story)
                    flash("Story has succesfully been updated!")
                    return redirect(url_for("profile", username=session["user"]))
                
                # if page is opened, find values, and post to form
                return render_template("edit_story.html", story=story, form=form)
    
        flash("Access denied. Create an account to edit stories", "error")
        flash("Or, login with your credentials below")
        return redirect(url_for("login"))


# delete story template route - coming from profile page
@app.route("/delete_story/<story_id>")
def delete_story(story_id):
        if "user" in session:
            if session["user"]:
                mongo.db.stories.remove({"_id": ObjectId(story_id)})
                flash("Story succesfully removed from database!")
                return redirect(url_for("profile", username=session["user"]))
        
        flash("Access denied. You are not allowed to remove this story", "error")
        flash("Login with your credentials below, to edit/remove stories")
        return redirect(url_for("login"))


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
        # check if email is already present in db
        existing_email_address = mongo.db.users.find_one(
            {"email_address": form.email_address.data.lower()})
        if existing_email_address:
            flash("Email address is already present, please choose another one, or reset password...")
            return redirect(url_for("register"))

        register = {
            "username": form.username.data.lower(),
            "email_address": form.email_address.data.lower(),
            "about_me": form.about_me.data.lower() or "Edit profile, if you want to enter a small bio",
            "avatar": form.avatar.data.lower() or "https://cdn.pixabay.com/photo/2016/08/08/09/17/avatar-1577909_1280.png",
            "tandc": form.terms_and_conditions.data,
            "password": generate_password_hash(form.password.data)
        }
        mongo.db.users.insert_one(register)

        session["user"] = form.username.data.lower()
        flash("Registration Succesful, welcome to the club!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html", form=form)


# profile template route
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    if "user" in session:
        if session["user"]:
            # grab the session users username from the db
            username = mongo.db.users.find_one(
                {"username": session["user"]})["username"]
            avatar = mongo.db.users.find_one(
                {"username": session["user"]})["avatar"]
            about_me = mongo.db.users.find_one(
                {"username": session["user"]})["about_me"]
            # Find stories written by user, and return to page
            stories_written = mongo.db.stories.find(
                {"username": session["user"]}).sort("_id", -1)
            return render_template("profile.html", stories_written=stories_written, username=username, about_me=about_me, avatar=avatar)
    
    flash("Access denied. Create an account to view profiles and your profile", "error")
    flash("Or, login with your credentials below")
    return redirect(url_for("login"))


# public profile template route
@app.route("/profile/public/<username>")
def public_profile(username):
    # grab username's about me
    username_about_me = mongo.db.users.find_one(
        {"username": username})["about_me"]
    # grab username's avatar
    username_avatar = mongo.db.users.find_one(
        {"username": username})["avatar"]

    return render_template("profile_public.html", username=username, username_avatar=username_avatar, username_about_me=username_about_me)
    

# profile edit template route
@app.route("/profile/<username>/edit", methods=["GET", "POST"])
def profile_edit(username):
        if "user" in session:
            if session["user"]:
                # grab the session users username from the db
                username = mongo.db.users.find_one(
                    {"username": session["user"]})["username"]
                # grab the session users username ID from the db
                username_id = mongo.db.users.find_one({"username": session["user"]})["_id"]
                # grab the session users username about_me details from the db
                username_default_value_about_me = mongo.db.users.find_one(
                    {"username": session["user"]})["about_me"]
                # grab the session users username avatar from the db
                username_default_value_avatar = mongo.db.users.find_one(
                    {"username": session["user"]})["avatar"]
                form = EditProfileForm(about_me=username_default_value_about_me, avatar=username_default_value_avatar)

            # I had issues with using set, and the following page helped me find a solution to this:
            # https://stackoverflow.com/questions/29837370/pymongo-update-one-syntax-error
                if form.validate_on_submit():
                    mongo.db.users.update({"_id": ObjectId(username_id)},
                                        {"$set":
                                        {"about_me": form.about_me.data or username_default_value_about_me,
                                        "avatar": form.avatar.data or username_default_value_avatar}})
                    flash("Profile succesfully updated!")
                    return redirect(url_for("profile", username=session["user"]))

                return render_template("profile_edit.html", username=username, form=form)
    
        flash("Access denied. Create an account to edit your profile", "error")
        flash("Or, login with your credentials below")
        return redirect(url_for("login"))


# About template route
@app.route("/about")
def about():
    return render_template("about_pages/about.html")


# Terms template route
@app.route("/terms")
def terms():
    return render_template("about_pages/terms.html")


# Contact template route
# Found help, for using flask-mail from 
# https://code.tutsplus.com/tutorials/intro-to-flask-adding-a-contact-page--net-28982
@app.route("/contact", methods=["GET", "POST"])
def contact():
    # Could not find a solution to if user or not user, with help of Robinz Alumni from Slack, this was solved
    # https://code-institute-room.slack.com/archives/C7JQY2RHC/p1605556229478600?thread_ts=1605556092.478500&cid=C7JQY2RHC
    if 'user' in session:
        # Get username values from db
        username = mongo.db.users.find_one({"username": session["user"]})["username"]
        email_address = mongo.db.users.find_one({"username": session["user"]})["email_address"]
        # Could not find a solution directly for passing values, found help from:
        # https://stackoverflow.com/questions/51027440/how-do-i-set-a-value-for-a-hidden-field-in-a-flask-form-using-wtf-quick-form
        # Get ContactForm from forms.py, insert username and email address
        form = ContactForm(username=username, email_address=email_address)

        if request.method == "POST":
            msg = Message(form.subject.data, sender=form.email_address.data, recipients=['michaeldijk@outlook.com'])
            msg.body = """
            From: %s <%s>
            ----
            Subject: %s 
            ----
            Description: %s
            """ % (form.username.data, form.email_address.data, form.subject.data, form.description.data)
            mail.send(msg)
    
            flash("Thank you for your message! We'll get back to you shortly")
            return render_template("about_pages/contact.html", form=form)
        
        return render_template("about_pages/contact.html", form=form)
    # If user is not logged in, return default values
    else:
        # Get ContactForm from forms.py
        form = ContactForm()
        if request.method == "POST":
            msg = Message(form.subject.data, sender=form.email_address.data, recipients=['michaeldijk@outlook.com'])
            msg.body = """
            From: %s <%s>
            Subject: %s
            ---
            Description: %s
            """ % (form.username.data, form.email_address.data, form.subject.data, form.description.data)
            mail.send(msg)

            flash("Thank you for your message! We'll get back to you shortly")
            return render_template("about_pages/contact.html", form=form)
        
        return render_template("about_pages/contact.html", form=form)


# Languages template route
@app.route("/languages")
def languages():
    return render_template("about_pages/languages.html")


# Error 403 template route
@ app.errorhandler(403)
def internal_error(error):
    return render_template('errors/403.html'), 403


# Error 404 template route
@ app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


# Error 500 template route
@ app.errorhandler(500)
def not_found(error):
    return render_template('errors/500.html'), 500


# logout template route
@ app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have succesfully been logged out!")
    session.pop("user")
    return redirect(url_for("login"))


# ######################################################
# ################ ADMIN SECTION BELOW #################
# ######################################################


# manage languages template route
@app.route("/admin/manage_languages", methods=["GET", "POST"])
def manage_languages():
    if "user" in session:
            if session["user"] == "admin":
                form = AddLanguageForm()
                if form.validate_on_submit():
                    language = {
                        "language_name": form.language.data
                    }
                    mongo.db.languages.insert_one(language)
                    flash("language succesfully added!!")
                    return redirect(url_for("manage_languages"))

                languages = mongo.db.languages.find().sort("_id", -1)

                return render_template("admin/manage_languages.html", languages=languages, form=form)
    
    flash("Access denied!", "error")
    return redirect(url_for("login"))


# edit language template route
@app.route("/admin/edit/edit_language/<language_id>", methods=["GET", "POST"])
def edit_language(language_id):
    if "user" in session:
            if session["user"] == "admin":
                language = mongo.db.languages.find_one({"_id": ObjectId(language_id)})
                form = EditLanguageForm(language=language["language_name"])

                if form.validate_on_submit():
                    language = {
                        "language_name": form.language.data
                    }
                    mongo.db.languages.update({"_id": ObjectId(language_id)}, language)
                    flash("Language has succesfully been updated!")
                    return redirect(url_for("manage_languages"))

                return render_template("admin/edit/edit_language.html", form=form, language=language)
    
    flash("Access denied!", "error")
    return redirect(url_for("login"))


# delete language template route - coming from manage language page
@app.route("/admin/edit/delete_language/<language_id>")
def delete_language(language_id):
    if "user" in session:
            if session["user"] == "admin":
                mongo.db.languages.remove({"_id": ObjectId(language_id)})
                flash("Language succesfully removed from database!")
                return redirect(url_for("manage_languages"))
        
    flash("Access denied.", "error")
    return redirect(url_for("login"))


# manage stories template route
@app.route("/admin/manage_stories")
def manage_stories():
    if "user" in session:
        if session["user"] == "admin":
            stories = mongo.db.stories.find().sort("_id", -1)

            return render_template("admin/manage_stories.html", stories=stories)

    flash("Access denied!", "error")
    return redirect(url_for("login"))


# edit story admin template route
@app.route("/admin/edit/edit_story/<story_id>", methods=["GET", "POST"])
def admin_edit_story(story_id):
    if "user" in session:
            if session["user"] == "admin":
                story = mongo.db.stories.find_one({"_id": ObjectId(story_id)})
                language = mongo.db.stories.find_one({"_id": ObjectId(story_id)})["language_name"]
                story_title = mongo.db.stories.find_one({"_id": ObjectId(story_id)})["story_title"]
                story_description = mongo.db.stories.find_one({"_id": ObjectId(story_id)})["story_description"]
                languages = mongo.db.languages.find().sort("language_name", 1)
                username_default_value_about_me = mongo.db.stories.find_one({"_id": ObjectId(story_id)})["username"]
                # Form with values from above
                form = EditStoryForm(languages=language, title=story_title, story=story_description)
                # Populate languages from database in alphabetic order
                form.languages.choices = [(item["language_name"]) for item in mongo.db.languages.find().sort("language_name", 1)]
                
                if form.validate_on_submit():
                    story = {
                        "username": username_default_value_about_me,
                        "language_name": form.languages.data,
                        "story_title": form.title.data,
                        "story_description": form.story.data
                    }
                    mongo.db.stories.update({"_id": ObjectId(story_id)}, story)
                    flash("Story has succesfully been updated!")
                    return redirect(url_for("manage_stories"))
                
                # if page is opened, find values, and post to form
                return render_template("admin/edit/edit_story.html", story=story, form=form)
    
    flash("Access denied.", "error")
    return redirect(url_for("login"))


# delete story admin template route - coming from manage stories page
@app.route("/admin/edit/delete_story/<story_id>")
def admin_delete_story(story_id):
    if "user" in session:
            if session["user"] == "admin":
                mongo.db.stories.remove({"_id": ObjectId(story_id)})
                flash("Story succesfully removed from database!")
                return redirect(url_for("manage_stories"))
        
    flash("Access denied.", "error")
    return redirect(url_for("login"))


# manage users template route
@app.route("/admin/manage_users")
def manage_users():
    if "user" in session:
        if session["user"] == "admin":
            users = mongo.db.users.find()
            return render_template("admin/manage_users.html", users=users)
    
    flash("Access denied!", "error")
    return redirect(url_for("login"))


# delete users admin template route - coming from manage users page
@app.route("/admin/edit/delete_user/<user_id>")
def delete_user(user_id):
    if "user" in session:
            if session["user"] == "admin":
                mongo.db.users.remove({"_id": ObjectId(user_id)})
                flash("User succesfully removed from database!")
                return redirect(url_for("manage_users"))
        
    flash("Access denied.", "error")
    return redirect(url_for("login"))

# delete user's stories admin template route - coming from manage users page
@app.route("/admin/edit/delete_user_stories/<username>")
def delete_user_stories(username):
    if "user" in session:
            if session["user"] == "admin":
                mongo.db.stories.delete_many({"username": (username)})
                flash("Stories of user succesfully removed from database!")
                return redirect(url_for("manage_users"))
        
    flash("Access denied.", "error")
    return redirect(url_for("login"))


# run app, with environment variables from env.py local,
# otherwise from settings in Heroku
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # don't forget to change debug = false
            # later onwards, when testing is complete
            debug=True)