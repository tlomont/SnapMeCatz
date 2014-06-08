from snapchat import Snapchat

#Get snapchat ready
name = 'snapmecatz'
password = 'fuckyoni'
s = Snapchat()
s.login(name, password)

#AddFriends
count = 0
update=s.get_updates()
for user in (update['added_friends']):
    s.add_friend(user['name'])
    count+=1
print(count)