#!/usr/bin/python3
"""Query Reddit API and prints the top ten hot posts of a subreddit."""
import re
import requests


def add_title(dictionary, hot_posts, word_list):
    """Add item into a list."""
    if len(hot_posts) == 0:
        return

    title = hot_posts[0]['data']['title'].lower().split()

    for word in word_list:
        key = word.lower()
        if key not in dictionary:
            dictionary[key] = 0
        dictionary[key] += title.count(key)

    hot_posts.pop(0)
    add_title(dictionary, hot_posts, word_list)


def recurse(subreddit, dictionary, word_list, after=None):
    """Query to Reddit API."""
    u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    params = {
        'after': after,
        'limit': 100
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    dic = res.json()
    hot_posts = dic['data']['children']
    add_title(dictionary, hot_posts, word_list)
    after = dic['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, word_list, after=after)


def count_words(subreddit, word_list):
    """Init function."""
    dictionary = {}

    recurse(subreddit, dictionary, word_list)

    list = sorted(dictionary.items(), key=lambda kv: kv[1], reverse=True)

    if len(list) != 0:
        for item in list:
            if item[1] != 0:
                print("{}: {}".format(item[0], item[1]))
    else:
        print("")
