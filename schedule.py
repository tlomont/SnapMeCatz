from snapchat import Snapchat
import getpass
import urllib
import pickle


friends=''

#login to snapchat
name = 'snapmecatz'
password = 'fuckyoni'
s = Snapchat()
s.login(name, password)

#Get list of friends
update=s.get_updates()
for a in ((update['updates_response'])['friends']):
	if (a['type']==1 or a['type']==0):
		friends+=a['name']+','


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
