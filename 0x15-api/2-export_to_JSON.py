#!/usr/bin/python3
"""Retrieve users all task and thier stat finally export into '.csv'."""
import json
import requests
import sys

if __name__ == "__main__":
    em_id = int(sys.argv[1])
    file_n = f"{em_id}.json"
    url = f"https://jsonplaceholder.typicode.com/todos?userId={em_id}"
    url2 = f"https://jsonplaceholder.typicode.com/users/{em_id}"
    response = requests.get(url)
    response1 = requests.get(url2)
    todo = response.json()
    user = response1.json()
    user_n = user.get("username")
    line = {em_id: []}
    for i in todo:
        dicti = {"task": i.get("title"),
                 "completed": i.get("completed"),
                 "user_name": user_n}
        line[em_id].append(dicti)
    with open(file_n, mode='w', newline='') as file:
        json.dump(line, file)
