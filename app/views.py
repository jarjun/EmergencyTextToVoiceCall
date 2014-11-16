from flask import render_template, Flask, request, redirect, flash
from app import app
from .forms import RequestForm
import requests
from twilio.rest import TwilioRestClient
import twilio.twiml
import urllib

account_sid = "ACed174aa4db08574d608df749cd16e3fd"
auth_token  = "d96a5e6b2722cac3116e0298c965efd0"
client = TwilioRestClient(account_sid, auth_token)
BASE_URL = "https://emergencytexttovoice.herokuapp.com/"

@app.route('/sms', methods=['GET', 'POST'])
def default():
	inputText = request.values.get('Body',None)
	modifiedText = urllib.quote(inputText)
	urlToMake = BASE_URL + "call/" + modifiedText
	client.calls.create(url = urlToMake , to="+17572823575", from_ = "+12039874014")
	return ""

@app.route('/submitted', methods=['GET', 'POST'])
def submitted():
	return render_template('submitted.html')

@app.route('/', methods=['GET', 'POST'])
def form():
	form = RequestForm()
	if form.validate_on_submit():
		#flash(form.address.data)
		inputText = form.address.data
		modifiedText = urllib.quote(inputText)
		urlToMake = BASE_URL + "call/" + modifiedText
		client.calls.create(url = urlToMake , to="+17572823575", from_ = "+12039874014")
		return redirect("/submitted")
	return render_template('request.html',
							title= 'Request',
							form= form)
@app.route('/call/<message>', methods=['GET', 'POST'])
def createTwiML(message):
	resp = twilio.twiml.Response()
	resp.say(message)
	return str(resp)


