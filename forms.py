from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.fields.simple import TextAreaField
# Import DataRequired for required field, length for max length,
# EqualTo for equal to password field, Regexp for checking for input,
# and NoneOf for removing certain user accounts
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp, NoneOf, URL, Optional


# Found help for using WTForms, from: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(),
                                                   Length(
                                                       min=5, max=15, message="Username, Minimum 5 maximum 15 characters."),
                                                   Regexp(
                                                       "^[a-zA-Z0-9]{5,15}$", flags=0, message="Username can only contain small letters, and numbers"),
                                                   # Found help for NoneOf on https://stackoverflow.com/questions/58464698/anyof-validation-in-flask
                                                   NoneOf(["admin", "root", "superuser", "adminaccount", "Administrator", "administrator"], message="Username is not permitted", values_formatter=None)])
    email_address = StringField("Email Address", validators=[DataRequired(), Email(
        message="Please type a correct email address", granular_message=False, check_deliverability=False, allow_smtputf8=True, allow_empty_local=False)])
    about_me = StringField("About Yourself", validators=[Optional(), Length(
        min=10, max=150, message="About yourself, minimum 10 characters, max 150 characters.")])
    avatar = StringField("Your Avatar", validators=[Optional(),
                                                    Length(
        min=5, max=150, message="Avatar URL Maximum 150 characters."),
        URL(require_tld=True, message="Avatar is not an domain.")])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=5, max=15, message="Password, Minimum 5 maximum 15 characters."),
                                                     Regexp("^[a-zA-Z0-9]{5,15}$", flags=0, message="Password can only contain small letters, and numbers")])
    password_confirm = PasswordField(
        "Confirm Password", validators=[DataRequired(),
                                        EqualTo("password", message="Passwords do not match.")])
    terms_and_conditions = BooleanField('Agree?', validators=[DataRequired(), ])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class EditProfileForm(FlaskForm):
    about_me = TextAreaField('About Yourself', validators=[Optional()])
    avatar = StringField("Your Avatar", validators=[Optional(),
                                                    Length(
        min=5, max=150, message="Avatar URL Maximum 150 characters."),
        URL(require_tld=True, message="Avatar is not an domain.")])
    submit = SubmitField("Update")


class NewStoryForm(FlaskForm):
    languages = SelectField('Programming Language', choices=[])
    title = StringField("Title", validators=[DataRequired(), Length(min=5, max=50, message="Cannot post story, if title is shorter than 5chars.")])
    story = TextAreaField('Story', validators=[DataRequired()])
    submit = SubmitField("Submit Story")


class EditStoryForm(FlaskForm):
    languages = SelectField('Programming Language', choices=[])
    title = StringField("Title", validators=[DataRequired(), Length(min=5, max=150, message="Cannot update story, if title field is blank.")])
    story = TextAreaField("Story", validators=[DataRequired()])
    submit = SubmitField("Update story")

class EditLanguageForm(FlaskForm):
    language = StringField("Language", validators=[DataRequired(), Length(min=3, max=150, message="Cannot update language, language needs to be 3 to 150chars.")])
    submit = SubmitField("Update language")


class AddLanguageForm(FlaskForm):
    language = StringField("Language", validators=[DataRequired(), Length(min=3, max=150, message="Cannot update language, language needs to be 3 to 150chars.")])
    submit = SubmitField("Add language")

class ContactForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email_address = StringField("Email Address", validators=[DataRequired(), Email(
        message="Please type a correct email address", granular_message=False, check_deliverability=False, allow_smtputf8=True, allow_empty_local=False)])
    subject = StringField("About Yourself", validators=[Optional(), Length(
        min=10, max=150, message="About yourself, minimum 10 characters, max 150 characters.")])
    description = TextAreaField("Username", validators=[DataRequired()])
    submit = SubmitField("Send message")
    