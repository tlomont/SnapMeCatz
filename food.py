
from snapchat import Snapchat
import getpass
import urllib
import re
import urllib2
from bs4 import BeautifulSoup

a=[]
hdr = { 'User-Agent' : 'super happy flair bot by /u/spladug' }



url = 'http://www.reddit.com/r/foodporn'
conn = urllib2.urlopen(urllib2.Request(url, headers=hdr))
html = conn.read()
soup = BeautifulSoup(html)
for elem in soup.findAll('a', href=re.compile('\.imgur\.com/[a-zA-Z0-9]')):
        a.append(elem['href'])


#choose url
from random import choice
url_final = choice(a)
while(".gif" in url_final):
        url_final = choice(urls)

# #Get snapchat ready
name = 'snapmefood'
password = 'fuckyoni'
recipient = 'plowcity,xoxuewei'
urllib.urlretrieve(url_final, "food.jpg")
pic = "food.jpg"
s = Snapchat()
s.login(name, password)

# Send a snapchat
media_id = s.upload(Snapchat.MEDIA_IMAGE, pic)
s.send(media_id, recipient)

