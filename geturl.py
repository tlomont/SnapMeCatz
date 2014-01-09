import re
import urllib2
from bs4 import BeautifulSoup
import urllib
import pickle

a=[]

if __name__ == "__main__":
        #TODO: change user agent string
        hdr = { 'User-Agent' : 'super happy flair bot by /u/spladug' }



        url = 'http://www.reddit.com/r/catpictures/top/'
        conn = urllib2.urlopen(urllib2.Request(url, headers=hdr))
        html = conn.read()
        soup = BeautifulSoup(html)
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

        url = 'http://www.reddit.com/r/kittens/top/?sort=top&t=week'
        conn = urllib2.urlopen(urllib2.Request(url, headers=hdr))
        html = conn.read()
        soup = BeautifulSoup(html)
        for elem in soup.findAll('a', href=re.compile('\.imgur\.com/[a-zA-Z0-9]')):
        	a.append(elem['href'])
        	#print elem['href']

        url = 'http://www.reddit.com/r/lolcats/'
        conn = urllib2.urlopen(urllib2.Request(url, headers=hdr))
        html = conn.read()
        soup = BeautifulSoup(html)
        for elem in soup.findAll('a', href=re.compile('\.imgur\.com/[a-zA-Z0-9]')):
                a.append(elem['href'])
                #print elem['href']

pickle.dump(a, open( "urls.p", "wb" ))
