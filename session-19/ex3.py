import http.client
import json

username = input("Please type a valid username: ")
HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
GITHUB_ID = username
METHOD = "GET"

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)

def get_repos():
    REPO = "/repos"

    conn.request(METHOD, ENDPOINT + GITHUB_ID + REPO, None, headers)

    r1 = conn.getresponse()

    text_json = r1.read().decode("utf-8")
    conn.close()

    repos = json.loads(text_json)

    repo_list = list()

    for i in range(len(repos)):
        repo_list.append(repos[i]["name"])

    repo_str = ', '.join(repo_list)
    print("\nThe repositories of {} are : {}".format(username, repo_str))

def get_commits():
    ENDPOINT = "/repos/{}/2018-19-PNE-practices/commits".format(username)

    conn.request(METHOD, ENDPOINT, None, headers)

    r1 = conn.getresponse()

    if r1.status == 404:
        print("\nThe 2018-19-PNE-practice was not found in the {} directory.".format(username))

    else:
        text_json = r1.read().decode("utf-8")
        conn.close()

        repos = json.loads(text_json)

        print("\nThe number of commits for the 2018-19-PNE-practices repo is {}.".format(len(repos)))

def get_user_data():
    conn.request(METHOD, ENDPOINT + GITHUB_ID, None, headers)

    r1 = conn.getresponse()

    if r1.status == 404:
        print("\nSorry, User not found")

    else:
        print()
        print("Response received: {} {}".format(r1.status, r1.reason))

        text_json = r1.read().decode("utf-8")
        conn.close()

        user = json.loads(text_json)

        login = user['login']
        name = user['name']
        bio = user['bio']
        nrepos = user['public_repos']

        print()
        print("User: {}".format(login))
        print("Real Name: {}".format(name))
        print("Repos: {}".format(nrepos))
        print("Bio: {}".format(bio))

        get_repos()
        get_commits()

get_user_data()
