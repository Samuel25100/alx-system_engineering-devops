#!/usr/bin/python3
"""Retrieve users all task and thier stat finally export into '.csv'."""
import json
import requests

if __name__ == "__main__":
    file_n = "todo_all_employees.json"
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    user = response.json()
    user_l = []
    line = {}
    for i in user:
        user_id = i.get("id")
        url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        response1 = requests.get(url)
        todo = response1.json()
        for j in todo:
            dicti = {"username": i.get("username"),
                     "task": j.get("title"),
                     "completed": j.get("completed")}
            user_l.append(dicti)
        line[str(user_id)] = user_l
    with open(file_n, mode='w') as file:
        json.dump(line, file)
