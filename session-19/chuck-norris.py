
import http.client
import json

def get_jokes():
    HOSTNAME = "api.icndb.com"
    ENDPOINT = "/jokes/random"
    METHOD = "GET"

    headers = {'User-Agent': 'http-client'}

    conn = http.client.HTTPSConnection(HOSTNAME)
    conn.request(METHOD, ENDPOINT, None, headers)

    r1 = conn.getresponse()

    if r1.reason == 'OK':
        pass

    else:

        print("Response received: ", end='')
        print(r1.status, r1.reason)
        print()

    text_json = r1.read().decode("utf-8")
    conn.close()

    joke = json.loads(text_json)

    print()
    print("Random Joke {}:".format(joke['value']['id']), joke['value']['joke'])

def number_jokes():
    HOSTNAME = "api.icndb.com"
    ENDPOINT = "/jokes/count"
    METHOD = "GET"

    headers = {'User-Agent': 'http-client'}

    conn = http.client.HTTPSConnection(HOSTNAME)
    conn.request(METHOD, ENDPOINT, None, headers)

    r1 = conn.getresponse()

    if r1.reason == 'OK':
        pass

    else:
        print()
        print("Response received: ", end='')
        print(r1.status, r1.reason)
        print()

    print()
    text_json = r1.read().decode("utf-8")
    conn.close()

    joke = json.loads(text_json)

    print("Number of jokes is", joke['value'])
    print()

def categories():
    HOSTNAME = "api.icndb.com"
    ENDPOINT = "/categories"
    METHOD = "GET"

    headers = {'User-Agent': 'http-client'}

    conn = http.client.HTTPSConnection(HOSTNAME)
    conn.request(METHOD, ENDPOINT, None, headers)

    r1 = conn.getresponse()

    if r1.reason == 'OK':
        pass

    else:
        print()
        print("Response received: ", end='')
        print(r1.status, r1.reason)
        print()

    text_json = r1.read().decode("utf-8")
    conn.close()

    joke = json.loads(text_json)
    categories = str(joke['value']).strip('[]')

    print('The categories in the web are', categories, end='.')
    print()

get_jokes()
number_jokes()
categories()