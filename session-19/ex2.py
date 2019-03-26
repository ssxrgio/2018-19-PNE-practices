import http.client
import json

def get_woeid(city):
    HOSTNAME = "www.metaweather.com"
    ENDPOINT = "/api/location/search/?query={}".format(city)
    METHOD = 'GET'

    headers = {'User-Agent': 'http-client'}

    conn = http.client.HTTPSConnection(HOSTNAME)
    conn.request(METHOD, ENDPOINT, None, headers)

    r1 = conn.getresponse()

    print()
    print("Response received: ", end='')
    print(r1.status, r1.reason)

    text_json = r1.read().decode("utf-8")
    conn.close()

    location = json.loads(text_json)
    weoid = str(location[0]['woeid'])

    return weoid

HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/"

LOCATION_WOEID = get_woeid(input('Type a valid city: ').lower())
METHOD = "GET"

headers = {'User-Agent': 'http-client'}
conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT + LOCATION_WOEID + '/', None, headers)

r1 = conn.getresponse()
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

text_json = r1.read().decode("utf-8")
conn.close()

weather = json.loads(text_json)
print(weather)


time = weather['time']

temp0 = weather['consolidated_weather'][0]
description = temp0['weather_state_name']
temp = temp0['the_temp']
place = weather['title']
sunset = weather['sun_set']

print()
print("Place: {}".format(place))
print("Time: {}".format(time))
print("Weather description: {}".format(description))
print("Current temp: {} degrees".format(temp))
print('Sunset time: {}'.format(sunset))
