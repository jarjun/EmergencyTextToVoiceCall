from flask import render_template, Flask, request, redirect, flash
from app import app
from .forms import RequestForm
import requests
from twilio.rest import TwilioRestClient
import twilio.twiml
'''
@app.route('/')
def default():
	return render_template("rootpage.html")

@app.route('/<name>')
def index(name):
	p = {"limit": 50}
	r = requests.get("https://api.twitch.tv/kraken/users/"+name+"/follows/channels", params = p)
	r = r.json()
	channellist = []
	for key in r["follows"]:
		streamname = key["channel"]["name"]
		stream = requests.get("https://api.twitch.tv/kraken/streams/" + streamname)
		stream = stream.json()
		if stream["stream"] != None:
			channellist.append((stream["stream"]["viewers"], streamname))

	channellist = sorted(channellist)
	fin = channellist[-1][1]
	return render_template("stream.html", top = fin)

@app.route('/<name>/<pos>')
def indexpos(name,pos):
	p = {"limit": 50}
	r = requests.get("https://api.twitch.tv/kraken/users/"+name+"/follows/channels", params = p)
	r = r.json()
	channellist = []
	for key in r["follows"]:
		streamname = key["channel"]["name"]
		stream = requests.get("https://api.twitch.tv/kraken/streams/" + streamname)
		stream = stream.json()
		if stream["stream"] != None:
			channellist.append((stream["stream"]["viewers"], streamname))

	channellist = sorted(channellist)
	fin = channellist[-int(pos)][1]
	return render_template("stream.html", top = fin)

'''
@app.route('/', methods=['GET', 'POST'])
def default():
	account_sid = "ACed174aa4db08574d608df749cd16e3fd"
	auth_token  = "d96a5e6b2722cac3116e0298c965efd0"
	client = TwilioRestClient(account_sid, auth_token)
	toGet = request.values.get('From',None)
	resp = twilio.twiml.Response()
	message = toGet
	resp.message(message)
	return str(resp)

@app.route('/form', methods=['GET', 'POST'])
def form():
	form = RequestForm()
	return render_template('request.html',
							title= 'Request',
							form= form)
	'''
	messages = client.messages.list()
	body = messages[0].body
	num = messages[0].from_
	return render_template("rootpage.html", message = body, fromNumber = num)
	'''


