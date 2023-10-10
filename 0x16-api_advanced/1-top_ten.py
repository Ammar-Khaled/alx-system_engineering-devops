#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    r = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json",
                     headers={'User-Agent': 'Mozilla/5.0'},
                     allow_redirects=False)

    if (r.status_code != 200):
        print('None')
        return

    dict = r.json()
    if 'data' not in dict.keys():
        print('None')
        return

    if 'children' not in dict['data'].keys():
        print('None')
        return

    i = 1
    for child in dict['data']['children']:
        if i <= 10:
            if 'data' not in child.keys():
                print('None')
                return

            if 'title' not in child['data']:
                print('None')
                return

            print(child['data']['title'])
            i += 1
        else:
            break
