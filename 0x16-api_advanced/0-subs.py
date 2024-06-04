#!/usr/bin/python3
"""Make query and return passed argumnet's subscriber"""
import requests
import json


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url)

    if response.status_code == 404:
        return 0
    else:
        result = response.json()
        return(result['data']['subscribers'])
