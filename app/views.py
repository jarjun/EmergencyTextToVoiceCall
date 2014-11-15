from flask import render_template
from app import app
import requests
from twilio.rest import TwilioRestClient
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
	messages = client.messages.list()
	body = messages[0].body
	num = messages[0].from_
	return render_template("rootpage.html", message = body, fromNumber = num)


