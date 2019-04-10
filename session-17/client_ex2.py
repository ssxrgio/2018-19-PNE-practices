# -- Example of a client that uses the HTTP.client library
# -- for requesting a JSON object and printing their
# -- contents
import http.client
import json
import termcolor

PORT = 8080
SERVER = 'localhost'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
conn.request("GET", "/listusers")

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body



# -- Create a variable with the data,
# -- form the JSON received

person = json.load(r1)    # info from jason read as a dictionary

for pers in person:
    termcolor.cprint("Name: ", "green", end=' ')
    print(person[pers][0]['Firstname'],person[pers][1]['Lastname'])
    termcolor.cprint("Age: ", "blue", end=' ')
    print(person[pers][2]['Age'])

    for i, num in enumerate(person[pers][3]["Phonenumber"]):   # with enumerate function the positions will be shown
        termcolor.cprint("User phone number:{} ".format(i),"red")
        termcolor.cprint("  Type :", "yellow", end='')
        print(num['type'])
        termcolor.cprint("  User phone number: ", "yellow", end='')
        print(num['number'])