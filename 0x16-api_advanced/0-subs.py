#!/usr/bin/python3
"""Make query and return passed argumnet's subscriber"""
import requests
import json


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        result = response.json().get("data")
        if ("after" in result):
            if result.get("after") is None:
                return 0
        return result.get("subscribers")
    else:
        return 0
