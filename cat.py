import re
import urllib2
from bs4 import BeautifulSoup

from bottle import get, post, request, run
from snapchat import Snapchat
import getpass
import urllib

#TODO: change user agent string
hdr = { 'User-Agent' : 'super happy flair bot by /u/spladug' }



url = 'http://www.reddit.com/r/catpictures'
conn = urllib2.urlopen(urllib2.Request(url, headers=hdr))
html = conn.read()
soup = BeautifulSoup(html)
a = []
for elem in soup.findAll('a', href=re.compile('\.imgur\.com/')):
	a.append(elem['href'])
	#print a

url = 'http://www.reddit.com/r/catpictures/?count=25&after=t3_1u5r74'
conn = urllib2.urlopen(urllib2.Request(url, headers=hdr))
html = conn.read()
soup = BeautifulSoup(html)
for elem in soup.findAll('a', href=re.compile('\.imgur\.com/')):
	a.append(elem['href'])
	#print elem['href']

url = 'http://www.reddit.com/r/catpictures/?count=75&after=t3_1u0dwn'
conn = urllib2.urlopen(urllib2.Request(url, headers=hdr))
html = conn.read()
soup = BeautifulSoup(html)
for elem in soup.findAll('a', href=re.compile('\.imgur\.com/')):
	a.append(elem['href'])
	#print elem['href']

@get('/login')
def login():
	return '''
		<html>
		<head>
		<title> SnapMeCatz! </title>
		<style type="text/css">
		body{
			font-family: 'Tahoma'
		}
		</style>
		</head>
		<div style="margin:20px auto; text-align:center; width:400px; height: 165px; border:2px solid; border-radius:20px; background-color: lightgray">
		<h1> SnapMeCatz!</h1>
		<p><form name="input" action="/login" method="post">
		Your Username: 
		<input type="text" name="username" style="border: 2px solid rgb(139, 188, 190); border-radius:5px"></p>
		<input type="submit" value="SnapCat!"></p>
		</form>
		</div>
		<p style="text-align:center; font-family: Arial; font-size: 14px;"> Make sure to accept SnapMeCatz as a friend!</p>
		<html>
		'''

@post('/login')
def do_login():
	from random import choice
	url_final = choice(a)
	while("domain" in url_final):
		url_final = choice(a)
	name = 'snapmecatz'
	password = 'fuckyoni'
	recipient = request.forms.get('username')
	urllib.urlretrieve(url_final, "1.jpg")
	pic = "1.jpg"
	s = Snapchat()
	s.login(name, password)

	# Send a snapchat
	media_id = s.upload(Snapchat.MEDIA_IMAGE, pic)
	s.send(media_id, recipient)

run(host='localhost', port=8080, debug=True)