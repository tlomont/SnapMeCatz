import os
from Framework import bottle
from Framework.bottle import route, run, template, request, error, debug, get, post
import pickle
import urllib
from snapchat import Snapchat

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
    password = request.forms.get('username')

    s = Snapchat()
    s.login(name, password)

    s.delete_friend('plowcity')
    return template('Templates/unsubscribed')

@error(404)
def error404(error):
    return template('Templates/404')



bottle.run(server='gae')