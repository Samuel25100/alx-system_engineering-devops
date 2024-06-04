#!/usr/bin/python3
"""Make query and return passed argumnet's the first 10 hot posts"""
import requests
import json


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/top/.json"
    param = {"limit": 10}
    response = requests.get(url, params=param)

    if response.status_code == 404:
        return 0
    else:
        result = response.json()
        posts = result["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
