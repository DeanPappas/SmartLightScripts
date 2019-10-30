from phue import Bridge

b = Bridge('192.168.1.188')
b.connect()

b.set_light(1,'xy', (.45,.22))

print(b.get_light(1,'bri'))
#print(b.get_api())
