#!/usr/bin/python3
"""Return information from api about employee todo list progress."""
import requests
import sys

if __name__ == "__main__":
    em_id = int(sys.argv[1])
    tot = 0
    done = 0
    title = []
    url = f"https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    result = response.json()
    url = f"https://jsonplaceholder.typicode.com/users/{em_id}"
    response1 = requests.get(url)
    user = response1.json()
    user_n = user.get('name')
    for dic in result:
        if dic.get("userId") == em_id:
            tot += 1
            if dic.get('completed') is True:
                done += 1
                title.append(dic.get('title'))
    print(f"Employee {user_n} is done with tasks({done}/{tot}):")
    for line in title:
        print(f"\t {line}")
