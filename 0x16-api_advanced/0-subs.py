#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    r = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                     headers={'User-Agent': 'Mozilla/5.0'},
                     allow_redirects=False)
    if (r.status_code != 200):
        return 0
    dict = r.json()
    if 'data' not in dict.keys():
        return 0
    if 'subscribers' not in dict['data'].keys():
        return 0
    return dict['data']['subscribers']
