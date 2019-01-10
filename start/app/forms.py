from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm): # não sei é preciso isto , vê o figma
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired("Please enter your name")])
    email = EmailField('Email', validators=[DataRequired("Please enter an email"),
     Email("Please enter a valid email")])
    phone = IntegerField('Phone Number') #TODO: Phone number validators
    # adicionar entrada do zip code
    submit = SubmitField('Submit')
