from snapchat import Snapchat
import pickle
import urllib
import getpass

friends=''

name = 'snapmecatz'
password = 'fuckyoni'

s = Snapchat()
s.login(name, password)

update=s.get_updates()
count=0
for a in ((update['updates_response'])['snaps']):
	if ('sn' in a):
		if a['st'] != 2:
			friends+=(a['sn'])+','

s.clear_feed()

print friends


#Get urls of images
urls = pickle.load( open('urls.p', 'rb'))

#choose url
from random import choice
url_final = choice(urls)
while(".gif" in url_final):
        url_final = choice(urls)

#Get snapchat ready
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
