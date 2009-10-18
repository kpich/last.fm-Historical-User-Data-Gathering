#!/usr/bin/python
"""takes a newline delimited file with usernames, grabs
   and prints the first 50 friends of each of those friends.
   usage: python crawl_friend_tree.py usernames.txt
"""

import pylast
import sys

API_KEY = "your-api-key"
API_SECRET ="your-api-secret"

def crawl_friends(init_username_filename):
    network = pylast.get_lastfm_network(api_key = API_KEY, api_secret = API_SECRET)
    for username in open(init_username_filename, 'r').readlines():
	crawl_user_tree(username.strip(), network)

def crawl_user_tree(username, network):
    for user in network.get_user(username).get_friends():
	if not user is None: print user.get_name()

if __name__ == '__main__':
    crawl_friends(sys.argv[1])
