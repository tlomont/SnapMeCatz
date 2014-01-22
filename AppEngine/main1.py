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
    name = 'snapmecatz'
    password = 'fuckyoni'

    s = Snapchat()
    s.login(name, password)

    s.add_friend(request.forms.get('username'))

    return template('Templates/sent')

@get('/about')
def about():
    return template('Templates/about')

@get('/sent')
def sent():
    return template('Templates/sent')

@get('/unsubscribe')
def unsubscribe():
    return template('Templates/unsubscribe')

@get('/unsubscribed')
def unsubscribe():
    return template('Templates/unsubscribed')

@post('/unsubscribe')
def do_unsubscribe():
    name = 'snapmecatz'
    password = 'fuckyoni'

    s = Snapchat()
    s.login(name, password)

    s.delete_friend(request.forms.get('username'))
    return template('Templates/unsubscribed')

@error(404)
def error404(error):
    return template('Templates/404')



bottle.run(server='gae')