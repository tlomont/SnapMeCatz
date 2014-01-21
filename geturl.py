import re
import urllib2
from bs4 import BeautifulSoup
import urllib
import pickle

a=[]
urllist=[]
if __name__ == "__main__":
        hdr = { 'User-Agent' : 'SnapMeCatz scraper' }



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

        url = 'http://www.reddit.com/r/catpictures/?count=25'
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
for i in a:
	if i not in urllist:
    		if not '0n5ajAm' in i:
			urllist.append(i)
pickle.dump(urllist, open( "urls.p", "wb" ))
