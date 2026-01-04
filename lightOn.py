from phue import Bridge

b = Bridge('')

lights = b.get_light_objects()

b.set_light(1,'on', True)
