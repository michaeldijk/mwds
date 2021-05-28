from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
# Import DataRequired for required field, length for max length, EqualTo for equal to password field, Regexp for checking for input, and NoneOf for removing certain user accounts
from wtforms.validators import DataRequired, Length, EqualTo, Regexp, NoneOf


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                            Length(min=5, max=15, message="Username, Minimum 5 maximum 15 characters."),
                            Regexp("^[a-zA-Z0-9]{5,15}$", flags=0, message="Username can only contain small letters, and numbers"),
                            NoneOf(["admin", "root", "superuser", "adminaccount", "Administrator", "administrator"], message="Username is not permitted", values_formatter=None)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=15, message="Password, Minimum 5 maximum 15 characters."),
                            Regexp("^[a-zA-Z0-9]{5,15}$", flags=0, message="Password can only contain small letters, and numbers")])
    password_confirm = PasswordField(
                       'Confirm Password', validators=[DataRequired(), 
                        EqualTo('password', message="Passwords do not match."), Length(min=5, max=15, message="Minimum 5 maximum 15 characters.")])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')