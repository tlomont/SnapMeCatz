from bottle import get, post, request, run
from snapchat import Snapchat
import getpass


@get('/login')
def login():
	return '''
		<form name="input" action="/login" method="post">
		Your Username: 
		<input type="text" name="username">
		Password:
		<input type="password" name="password">
		Recipient Username:
		<input type="text" name="friend">
		<input type="submit" value="Submit">
		</form>
		'''

@post('/login')
def do_login():
	name = request.forms.get('username')
	password = request.forms.get('password')
	friend = request.forms.get('friend')
	s = Snapchat()
	s.login(name, password)

	# Send a snapchat
	media_id = s.upload(Snapchat.MEDIA_IMAGE, pic)
	s.send(media_id, friend)

run(host='localhost', port=8080, debug=True)
