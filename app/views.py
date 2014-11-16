from flask import render_template, Flask, request, redirect, flash
from app import app
from .forms import RequestForm
import requests
from twilio.rest import TwilioRestClient
import twilio.twiml
import urllib
import math
import requests
import sys

'''
@author Arjun Jain
@author Chris Bernt
@author Greg Lyons
@author Wesley Valentine
'''

account_sid = "ACed174aa4db08574d608df749cd16e3fd"
auth_token  = "d96a5e6b2722cac3116e0298c965efd0"
client = TwilioRestClient(account_sid, auth_token)
BASE_URL = "https://emergencytexttovoice.herokuapp.com/"

@app.route('/sms', methods=['GET', 'POST'])
def default():
	inputText = request.values.get('Body',None)
	location = findClosestPSAP(extractAddress(inputText))
	modifiedText = urllib.quote("P SAP Location is " + location + "." + "Your Message is " + inputText)
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
		location = findClosestPSAP(extractAddress(inputText))
		modifiedText = urllib.quote("P SAP Location is " + location + "." + "Your Message is " + inputText)
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





def distance(lat1, lng1, lat2, lng2):
    """
        Calculates distance in miles between two lat, long pairs
        Thanks to Philipp Jahoda of StackOverflow.com.
    """
    
    earthRadius = 3958.75
    
    dLat = math.radians(lat2 - lat1)
    dLng = math.radians(lng2 - lng1)
    
    sinDLat = math.sin(dLat / 2)
    sinDLng = math.sin(dLng / 2)
    
    a = (sinDLat ** 2) + (sinDLng ** 2) * math.cos(math.radians(lat1)) * math.cos(math.radians(lat2))
    c = 2 * math.atan2(a ** .5, (1-a) ** .5)
    
    dist = earthRadius * c
    
    return dist

def geocode(loc):
    url = "https://maps.googleapis.com/maps/api/geocode/json?parameters"
    
    query_params = { 'address' : loc,
                    'sensor': 'false'
                    }
    response = requests.get(url, params = query_params)
    geoData = response.json()
    #print geoData
    lat = geoData['results'][0]['geometry']['location']['lat']
    lng = geoData['results'][0]['geometry']['location']['lng']
    latLong = str(lat) + "," + str(lng)
    #print loc + ": " + latLong
    return latLong

def extractAddress(message):
    url = "https://extract-beta.api.smartystreets.com/"
    
    query_params = {
                    "auth-id" : "6e1411df-8d1e-4928-93c2-a690e3176b84",
                    "auth-token" : "TKhLiK6xt76gfTGAQRi3",
                    "input": message
                   }
    
    response = requests.get(url, params = query_params)
    addressData = response.json()
    return addressData["addresses"][0]["text"]


def findClosestPSAP(location):
    try:
        latLong = geocode(location).split(",")
    except:
        return "Bad location."
        
    myLat = float(latLong[0].strip())
    myLong = float(latLong[1].strip())
    
    f = open("PSAPData.txt")
    lines = f.readlines()
    bestDist = sys.maxint
    bestPSAP = ""
    PSAPAddress = ""
    
    for line in lines:
        lines = line.split(",")
        curDist = distance(myLat, myLong, float(lines[6]), float(lines[7]))
        if curDist < bestDist:
            bestDist = curDist
            bestPSAP = lines[0]
            PSAPAddress = lines[1] + ", " + lines[4] + ", " + lines[2]
    
    return bestPSAP + "; " + PSAPAddress


