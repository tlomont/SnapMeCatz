import os
from Framework import bottle
from Framework.bottle import route, run, template, request, error, debug, get, post
import pickle
import urllib
from snapchat import Snapchat
from google.appengine.runtime import apiproxy_errors
from google.appengine.api import mail


@get('/')
def index():
    return template('Templates/index')

@post('/')
def send():
    name = 'snapmecatz'
    password = ''

    s = Snapchat()
    try:
        s.login(name, password)
    except:
        message = mail.EmailMessage(sender="SnapMeCatz <tommy.lomont@gmail.com>",
                                    subject=("Subscriber "+request.forms.get('username')))

        message.to = "SnapMeCatz <snapmecatz1@gmail.com>"

        message.body = request.forms.get('username')

        message.send()

    try:
        s.add_friend(request.forms.get('username'))
    except:
        message = mail.EmailMessage(sender="SnapMeCatz <tommy.lomont@gmail.com>",
                                    subject=("Subscriber "+request.forms.get('username')))

        message.to = "SnapMeCatz <snapmecatz1@gmail.com>"

        message.body = request.forms.get('username')

        message.send()


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
    try:
        s.login(name, password)
    except:
        message = mail.EmailMessage(sender="SnapMeCatz <tommy.lomont@gmail.com>",
                                    subject=("Unsubscribe "+request.forms.get('username')))

        message.to = "SnapMeCatz <snapmecatz1@gmail.com>"

        message.body = request.forms.get('username')

        message.send()

    try:
        s.delete_friend(request.forms.get('username'))
    except:
        message = mail.EmailMessage(sender="SnapMeCatz <tommy.lomont@gmail.com>",
                                    subject=("Unsubscribe "+request.forms.get('username')))

        message.to = "SnapMeCatz <snapmecatz1@gmail.com>"

        message.body = request.forms.get('username')

        message.send()

    return template('Templates/unsubscribed')

@error(404)
def error404(error):
    return template('Templates/404')



bottle.run(server='gae')