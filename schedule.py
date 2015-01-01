from snapchat import Snapchat
import geturl
import getpass
import urllib
import pickle

#Get urls of images
geturl.get_url()
urls = pickle.load( open('urls.p', 'rb'))

#choose url
from random import choice
url_final = choice(urls)
while(".gif" in url_final):
        url_final = choice(urls)

#Get snapchat ready
name = 'snapmecatz'
password = $password
urllib.urlretrieve(url_final, "1.jpg")
pic = "1.jpg"
s = Snapchat()
s.login(name, password)

#Get list of friends and send for every 100
friends = ''
count = 0
update=s.get_updates()
media_id = s.upload(Snapchat.MEDIA_IMAGE, pic)
for a in (update['friends']):
    if (a['type']==0):
        friends+=a['name']+','
        if (count > 99):
            media_id = s.upload(Snapchat.MEDIA_IMAGE, pic)
	    s.send(media_id, friends)
            count = 0
            friends = ''
        count+=1
media_id = s.upload(Snapchat.MEDIA_IMAGE, pic)
s.send(media_id, friends)
