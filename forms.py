from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirm = PasswordField(
                       'Confirm Password', validators=[DataRequired(), 
                        EqualTo('password', message='Passwords must be the same.')])
    submit = SubmitField('Register')

