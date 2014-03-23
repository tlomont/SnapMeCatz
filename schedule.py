from snapchat import Snapchat
import geturl
import getpass
import urllib
import pickle


friends = friends2 = friends3 = friends4 = friends5 = friends6 = friends7 = friends8 = friends9 = ''

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
        if (count < 100):
            friends+=a['name']+','
        elif (count < 200):
            friends2+=a['name']+','
        elif (count < 300):
            friends3+=a['name']+','
        elif (count < 400):
            friends4+=a['name']+','
        elif (count < 500):
            friends5+=a['name']+','
        elif (count < 600):
            friends6+=a['name']+','
        elif (count < 700):
            friends7+=a['name']+','
        elif (count < 800):
            friends8+=a['name']+','
        else:
            friends9+=a['name']+','
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

recipient = friends3
media_id = s.upload(Snapchat.MEDIA_IMAGE, pic)
s.send(media_id, recipient)

recipient = friends4
media_id = s.upload(Snapchat.MEDIA_IMAGE, pic)
s.send(media_id, recipient)

recipient = friends5
media_id = s.upload(Snapchat.MEDIA_IMAGE, pic)
s.send(media_id, recipient)

recipient = friends6
media_id = s.upload(Snapchat.MEDIA_IMAGE, pic)
s.send(media_id, recipient)

recipient = friends7
media_id = s.upload(Snapchat.MEDIA_IMAGE, pic)
s.send(media_id, recipient)

recipient = friends8
media_id = s.upload(Snapchat.MEDIA_IMAGE, pic)
s.send(media_id, recipient)

recipient = friends9
media_id = s.upload(Snapchat.MEDIA_IMAGE, pic)
s.send(media_id, recipient)
