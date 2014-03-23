from snapchat import Snapchat
import getpass

name = raw_input('Username:')
password = getpass.getpass('Password:')
friend = raw_input('Friend:')
pic = raw_input('File name:')

s = Snapchat()
s.login(name, password)

# Send a snapchat
media_id = s.upload(Snapchat.MEDIA_IMAGE, pic)
s.send(media_id, friend)

print 'Yeeeee!'
