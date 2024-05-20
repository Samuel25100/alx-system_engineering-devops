#!/usr/bin/python3
"""Retrieve users all task and thier stat finally export into '.csv'."""
import csv
import requests
import sys

if __name__ == "__main__":
    em_id = int(sys.argv[1])
    file_n = f"{em_id}.csv"
    url = f"https://jsonplaceholder.typicode.com/todos?userId={em_id}"
    url2 = f"https://jsonplaceholder.typicode.com/users/{em_id}"
    response = requests.get(url)
    response1 = requests.get(url2)
    todo = response.json()
    user = response1.json()
    user_n = user.get("username")
    line = []
    for i in todo:
        line.append([em_id, user_n, i.get("completed"), i.get("title")])
    with open(file_n, mode='w', newline='') as file:
        writer = csv.writer(file,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for i in line:
            writer.writerow(i)
