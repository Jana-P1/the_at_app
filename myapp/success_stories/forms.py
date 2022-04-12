from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class SuccessStoryForm(FlaskForm):
  title = StringField('Title', validators=[DataRequired()])
  story = TextAreaField('Story', validators=[DataRequired()])
  submit = SubmitField('Submit')
