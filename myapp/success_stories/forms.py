from typing import Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class SuccessStoryForm(FlaskForm):
  title = StringField('Title', validators=[DataRequired()]),
  story = TextAreaField('Text', validators=[DataRequired()]),
  submit = SubmitField('Post')
