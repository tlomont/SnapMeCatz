from snapchat import Snapchat

f = open('username.txt', 'r')
arr = []
for line in f:
        arr.append(line.strip('\n'))
f.close()

s = Snapchat()
s.login('snapmecatz', 'fuckyoni')

for l in arr:
        media_id = s.upload(Snapchat.MEDIA_IMAGE, '1.jpg')
        s.send(media_id,l)
        print l
