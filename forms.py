from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, AnyOf, URL

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField('Pet name', validators=[InputRequired()])
    species = SelectField('Species', choices=['cat', 'dog', 'porcupine'])
    photo_url = StringField('Photo URL', validators=[URL(message='Please enter a valid photo url.'), Optional()])
    age = IntegerField('Age', validators=[NumberRange(min=0, max=30, message='We are only accepting pets between the ages of 0 and 30.'), Optional()])
    notes = TextAreaField('Notes')

class EditPetForm(FlaskForm):
    """Form for editing some of the pet fields."""

    photo_url = StringField('Photo URL', validators=[URL(message='Please enter a valid photo url.'), Optional()])
    notes = TextAreaField('Notes')
    available = BooleanField()