from snapchat import Snapchat

f = open('username.txt', 'r')
arr = []
for line in f:
	arr.append(line)
f.close()

s = Snapchat()
s.login('snapmecatz', 'fuckyoni')
media_id = s.upload(Snapchat.MEDIA_IMAGE, '1.jpg')
for l in arr:
	s.send(media_id,l)
	print l
