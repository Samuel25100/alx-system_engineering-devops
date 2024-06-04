#!/usr/bin/python3
"""Return list containing the titles of all hot articles"""
import requests
import json


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    params = {"after": after, "limit": 100}
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 404:
        return None
    data = response.json()
    after = data["data"]["after"]
    if after is None:
        return hot_list
    else:
        posts = data["data"]["children"]
        for post in posts:
            hot_list.append(post["data"]["title"])
        return recurse(subreddit, hot_list, after)
