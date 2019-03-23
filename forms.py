from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), length(min=2, max=20)])

    password = PasswordField('Password', validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    email = StringField('Email', validators=[DataRequired(), Email()])

    submit = SubmitField('Sign Up')



class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

