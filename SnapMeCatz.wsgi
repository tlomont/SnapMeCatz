import sys
import os
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))
sys.path.append('/var/www/SnapMeCatz')


import bottle
# ... build or import your bottle application here ...
from bottle import get, post, request, run, default_app, template
from snapchat import Snapchat
import getpass
import urllib
import pickle

bottle.TEMPLATES.clear()

#urls = pickle.load( open('urls.p', 'rb'))

@get('/')
def index():
        return template('Templates/index')

@post('/')
def send():
        urls = pickle.load( open('urls.p', 'rb'))
        from random import choice
        url_final = choice(urls)
        while(".gif" in url_final):
                url_final = choice(urls)
        name = 'snapmecatz'
        password = 'fuckyoni'
        recipient = request.forms.get('username')
        urllib.urlretrieve(url_final, "1.jpg")
        pic = "1.jpg"
        s = Snapchat()
        s.login(name, password)

        #add username to file
        #f = open('username.txt','a')
        #f.write(recipient+'\n')

        # Send a snapchat
        media_id = s.upload(Snapchat.MEDIA_IMAGE, pic)
        s.send(media_id, recipient)

        return template('Templates/sent')

@get('/about')
def about():
        return template('Templates/about')

@get('/unsubscribe')
def unsubscribe():
    return template('Templates/unsubscribe')

@post('/unsubscribe')
def do_unsubscribe():
    name = 'snapmecatz'
    password = 'fuckyoni'

    s = Snapchat()
    s.login(name, password)

    s.delete_friend('plowcity')
    return template('Templates/unsubscribed')

from bottle import error
@error(404)
def error404(error):
    return template('Templates/404')


# Do NOT use bottle.run() with mod_wsgi
application = bottle.default_app()
