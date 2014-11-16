from flask import render_template, Flask, request, redirect, flash
from app import app
from .forms import RequestForm
import requests
from twilio.rest import TwilioRestClient
import twilio.twiml

account_sid = "ACed174aa4db08574d608df749cd16e3fd"
auth_token  = "d96a5e6b2722cac3116e0298c965efd0"
client = TwilioRestClient(account_sid, auth_token)

@app.route('/', methods=['GET', 'POST'])
def default():
	toGet = request.values.get('Body',None)
	resp = twilio.twiml.Response()
	message = client.messages.create(to="+17572823575", from_ = "+12039874014",body=toGet)
	resp.message(message)
	return str(resp)

@app.route('/form', methods=['GET', 'POST'])
def form():
	form = RequestForm()
	if form.validate_on_submit():
		#flash(form.address.data)
		resp = twilio.twiml.Response()
		message = client.messages.create(to="+17572823575", from_ = "+12039874014",body=form.address.data)
		#resp.message(message)
	return render_template('request.html',
							title= 'Request',
							form= form)
	'''
	messages = client.messages.list()
	body = messages[0].body
	num = messages[0].from_
	return render_template("rootpage.html", message = body, fromNumber = num)
	'''


