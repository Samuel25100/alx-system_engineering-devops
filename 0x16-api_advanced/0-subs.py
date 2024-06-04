#!/usr/bin/python3
"""Make query and return passed argumnet's subscriber"""
import requests
import json


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {'User-Agent': "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    response = requests.get(url, headers=header, allow_redirects=False)

    if response.status_code == 404:
        return 0
    result = response.json().get("data")
    if ("after" in result):
        if result.get("after") is None:
            return 0
    return result.get("subscribers")
