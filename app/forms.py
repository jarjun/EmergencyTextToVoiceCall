from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class RequestForm(Form):
	street = StringField('street', description = "Street", validators=[DataRequired()])
	state = StringField('state', description = "State", validators=[DataRequired()])
	zipCode = StringField('zipCode', description = "Zip Code", validators=[DataRequired()])
	desc = StringField('desc', description = "Situacion", validators=[DataRequired()])
