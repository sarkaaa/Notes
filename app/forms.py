from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length
from .models import User

class PostForm(Form):
	post = StringField('post', validators=[DataRequired()])