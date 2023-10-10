#!/usr/bin/python3
"""Return a list of titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Print the titles of all hot posts for a given subreddit."""
    r = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json",
                     headers={'User-Agent': 'Mozilla/5.0'},
                     params={'after': after},
                     allow_redirects=False)

    if (r.status_code != 200):
        return None

    dict = r.json()
    if 'data' not in dict.keys():
        return None

    if 'children' not in dict['data'].keys():
        return None
    hot_posts = dict['data']['children']

    for post in hot_posts:
        hot_list.append(post['data']['title'])

    after = dict['data']['after']
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after=after)
