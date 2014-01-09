import re
import urllib2
from bs4 import BeautifulSoup
from snapchat import Snapchat
import getpass
import urllib

#TODO: change user agent string
hdr = { 'User-Agent' : 'super happy flair bot by /u/spladug' }



url = 'http://www.reddit.com/r/catpictures/top/'
conn = urllib2.urlopen(urllib2.Request(url, headers=hdr))
html = conn.read()
soup = BeautifulSoup(html)
a = []
for elem in soup.findAll('a', href=re.compile('\.imgur\.com/[a-zA-Z0-9]')):
        a.append(elem['href'])
        #print a

url = 'http://www.reddit.com/r/cats/top/'
conn = urllib2.urlopen(urllib2.Request(url, headers=hdr))
html = conn.read()
soup = BeautifulSoup(html)
for elem in soup.findAll('a', href=re.compile('\.imgur\.com/[a-zA-Z0-9]')):
        a.append(elem['href'])
        #print elem['href']

url = 'http://www.reddit.com/r/catpictures/?count=25&after=t3_1uigsy'
conn = urllib2.urlopen(urllib2.Request(url, headers=hdr))
html = conn.read()
soup = BeautifulSoup(html)
for elem in soup.findAll('a', href=re.compile('\.imgur\.com/[a-zA-Z0-9]')):
        a.append(elem['href'])
        #print elem['href']

from random import choice
url_final = choice(a)
while("domain" in url_final):
        url_final = choice(a)
name = 'snapmecatz'
password = 'fuckyoni'
recipient = 'plowcity,waleepmaleep'
urllib.urlretrieve(url_final, "1.jpg")
pic = "1.jpg"
s = Snapchat()
s.login(name, password)

# Send a snapchat
media_id = s.upload(Snapchat.MEDIA_IMAGE, pic)
s.send(media_id, recipient)
