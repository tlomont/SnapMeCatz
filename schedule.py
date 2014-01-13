from snapchat import Snapchat
import getpass
import urllib
import pickle

urls = pickle.load( open('urls.p', 'rb'))

from random import choice
url_final = choice(urls)
while(".gif" in url_final):
        url_final = choice(urls)
with open ("php/friends.txt", "r") as myfile:
	friends=myfile.read()
name = 'snapmecatz'
password = 'fuckyoni'
recipient = friends
urllib.urlretrieve(url_final, "1.jpg")
pic = "1.jpg"
s = Snapchat()
s.login(name, password)

# Send a snapchat
media_id = s.upload(Snapchat.MEDIA_IMAGE, pic)
s.send(media_id, recipient)
