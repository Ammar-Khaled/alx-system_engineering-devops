#!/usr/bin/python3
"""
This module uses the "JSONPlaceholder" REST API
for a given employee ID accepted as an integer argument
and saves information about his/her TODO list progress in a json file.
"""


if __name__ == "__main__":
    import json
    from requests import get

    url = 'https://jsonplaceholder.typicode.com/'
    saving_file = 'todo_all_employees.json'

    data = {}
    for emp_id in range(1, 11):
        response = get(url + f'users/{emp_id}')
        emp_username = response.json().get('username')

        response = get(url + f'users/{emp_id}/todos')
        emp_todos = response.json()
        to_write_todos = []
        for todo in emp_todos:
            to_write_todos.append({"username": emp_username,
                                   "task": todo.get('title'),
                                   "completed": todo.get('completed')})

        data[emp_id] = to_write_todos

    with open(saving_file, 'w', newline='') as f:
        json.dump(data, f)
