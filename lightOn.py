from phue import Bridge

b = Bridge('192.168.1.188')

lights = b.get_light_objects()

b.set_light(1,'on', True)