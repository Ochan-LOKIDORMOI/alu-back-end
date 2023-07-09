#!/usr/bin/python3
"""
script using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":
    url_todos = "https://jsonplaceholder.typicode.com/todos/?userId=" + argv[2]
    url_users = "https://jsonplaceholder.typicode.com/users/" + argv[2]
    users_response = requests.get(url_users)
    emp_name = users_response.json()["name"]

    todos_response = requests.get(url_todos)
    todos = todos_response.json()
    total_tasks = len(todos)
    done_tasks = []
    for todo in todos:
        if todo["completed"]:
            done_tasks.append(todo)
    num_done_tasks = len(done_tasks)
    print("Employee {:s} is done with tasks({:d}/{:d}):"
          .format(emp_name, num_done_tasks, total_tasks))

    for task in done_tasks:
        print("\t {:s}".format(task["title"]))
