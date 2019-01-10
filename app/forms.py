from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired("Please enter your name")])
    email = EmailField('Email', validators=[DataRequired("Please enter an email"),
     Email("Please enter a valid email")])
    phone = IntegerField('Phone Number', validators=[DataRequired("Please enter a phone number")]) #TODO: Phone number validators
    zip_code = IntegerField('Zip Code', validators=[DataRequired("Please enter a zip code")])
    submit = SubmitField('Submit')
