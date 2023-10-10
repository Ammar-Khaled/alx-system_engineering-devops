#!/usr/bin/python3
"""Return a list of titles of all hot articles for a given subreddit."""
import requests


def add_title(hot_list, hot_posts):
    """Add the titles of hot_posts to hot_list."""
    if len(hot_posts) == 0:
        return

    hot_list.append(hot_posts[0]['data']['title'])
    hot_posts.pop(0)
    add_title(hot_list, hot_posts)

def recurse(subreddit, hot_list=[], after=None):
    """Print the titles of all hot posts for a given subreddit."""
    r = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json",
                     headers={'User-Agent': 'Mozilla/5.0'},
                     params={'after': after},
                     allow_redirects=False)

    if (r.status_code != 200):
        return None

    dict = r.json()
    hot_posts = dict['data']['children']

    add_title(hot_list, hot_posts)

    after = dict['data']['after']
    if not after:
        return hot_list

    return recurse(subreddit, hot_list=hot_list, after=after)
