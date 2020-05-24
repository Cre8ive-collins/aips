from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField 
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField('Sign-in')

class RegisterationForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo(password)])
    email = StringField(validators=[DataRequired(), Email()])
    name = StringField(validators=[DataRequired()])
    submit = SubmitField('Sign-up') 
