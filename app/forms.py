from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class RequestForm(Form):
	inputText = TextAreaField('inputText', validators=[DataRequired()])
