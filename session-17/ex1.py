
import json
import termcolor

f = open("ex1.json", "r")

person = json.load(f)    # info from jason read as a dictionary

for pers in person:
    termcolor.cprint("Name: ", "green", end=' ')
    print(person[pers][0]['Firstname'], person[pers][1]['Lastname'])
    termcolor.cprint("Age: ", "blue", end=' ')
    print(person[pers][2]['Age'])

    for i, num in enumerate(person[pers][3]["Phonenumber"]):   # with enumerate function the positions will be shown
        termcolor.cprint("User phone number: {} ".format(i), "red")
        termcolor.cprint("  Type: ", "cyan", end='')
        print(num['type'])
        termcolor.cprint("  User phone number: ", "cyan", end='')
        print(num['number'])

    print()