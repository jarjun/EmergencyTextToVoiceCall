from flask.ext.wtf import Form
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class RequestForm(Form):
	inputText = TextAreaField('inputText', validators=[DataRequired()])
