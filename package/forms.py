from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from package.dbmodels import Tracks, Path




class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField('Sign-in')

class CreateUserForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo(password)])
    email = StringField(validators=[DataRequired(), Email()])
    name = StringField(validators=[DataRequired()])
    submit = SubmitField('Sign-up') 


class ReadUserForm(FlaskForm):
    username = StringField()
    email = StringField()

class UpdateUserForm(FlaskForm):
    username = StringField()
    email = StringField()

class UpdatePostForm(FlaskForm):
    title = StringField(validators=[DataRequired()])
    description = StringField()
    body = StringField()
    subject = StringField()
    creator = StringField()
    track = StringField()
    image = StringField()
    video = StringField()
    submit = SubmitField('Update Post')

class DeletePostForm(FlaskForm):
    title = StringField(validators=[DataRequired()])

class DeleteUserForm(FlaskForm):
    username = StringField()
    email = StringField()
