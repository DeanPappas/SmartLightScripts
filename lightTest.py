from phue import Bridge

b = Bridge('')
b.connect()

#b.set_light(1,'xy', (.45,.22))

print(b.get_light(1,'xy'))
#print(b.get_api())
