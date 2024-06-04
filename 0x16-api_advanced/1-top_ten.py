#!/usr/bin/python3
"""Make query and return passed argumnet's the first 10 hot posts"""
import requests
import json


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    param = {"limit": 10}
    response = requests.get(url, headers=headers,
                            params=param, allow_redirects=False)

    if response.status_code == 200:
        result = response.json()
        posts = result["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
    else:
        print("None")
