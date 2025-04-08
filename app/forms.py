# Add any form classes for Flask-WTF here

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf.file import FileAllowed

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired(message="Movie Requires a Title")])
    description = TextAreaField('Description', validators=[DataRequired(message="Movie Requires a Description")])
    poster = FileField('Poster', validators=[
        FileAllowed(['jpg', 'png', 'jpeg'], 'Only image files are allowed.'),
        DataRequired(message="Movie Requires a Poster")
    ])
