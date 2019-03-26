# Example of getting information about the weather of
# a location

import http.client
import json

# -- API information
city = input('Type a valid city: ').lower()
HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/search/?query={}".format(city)
METHOD = 'GET'

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT + '/', None, headers)

r1 = conn.getresponse()

print()
print("Response received: ", end='')
print(r1.status, r1.reason)

text_json = r1.read().decode("utf-8")
conn.close()

weather = json.loads(text_json)
print(weather)
