from phue import Bridge
import requests
import json

response = requests.get("https://discovery.meethue.com/")
response.raise_for_status()
data = response.json()

hub_ip = data[0]["internalipaddress"]

b = Bridge(hub_ip)
b.connect()
# Get list of light # keys
light_data = b.get_api()['lights']
#b.set_light(1,'xy', (.45,.22))
# Create JSON of hub API call
# with open("lights.json", "w") as file:
#     json.dump(b.get_api()["lights"], file, indent=4)

# Get user names for lights
for light in b.get_api()['lights']:
    print(b.get_api()['lights'][light]['name'])

print(b.get_light(1,'xy'))
print(b.get_api())
print(b.get_api())