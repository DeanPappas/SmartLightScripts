from phue import Bridge

b = Bridge('192.168.1.188')
b.connect()

b.set_light(1,'xy', (.01,.01))


