from snapchat import Snapchat
import geturl
import getpass
import urllib
import pickle


friends = friends2 =''

#login to snapchat
name = 'snapmecatz'
password = 'fuckyoni'
s = Snapchat()
s.login(name, password)

#Get list of friends
count = 0
update=s.get_updates()
for a in (update['friends']):
    if (a['type']==0):
        if (count < 410):
            friends+=a['name']+','
        else:
            friends2+=a['name']+','
        count+=1


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
password = 'fuckyoni'
recipient = friends
urllib.urlretrieve(url_final, "1.jpg")
pic = "1.jpg"
s = Snapchat()
s.login(name, password)

# Send a snapchat
media_id = s.upload(Snapchat.MEDIA_IMAGE, pic)
s.send(media_id, recipient)

#send second group
recipient = friends2
media_id = s.upload(Snapchat.MEDIA_IMAGE, pic)
s.send(media_id, recipient)
