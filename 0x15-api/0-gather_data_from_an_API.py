#!/usr/bin/python3
"""
This module uses the "JSONPlaceholder" REST API
for a given employee ID accepted as an integer argument
and returns information about his/her TODO list progress.
"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    url = 'https://jsonplaceholder.typicode.com/'
    emp_id = argv[1]

    response = get(url + f'users/{emp_id}')
    emp_name = response.json().get('name')

    response = get(url + f'users/{emp_id}/todos')
    emp_todos = response.json()
    completed_todos = []
    for todo in emp_todos:
        if todo.get('completed'):
            completed_todos.append(todo)

    print(f'Employee {emp_name} is done with '
          f'tasks({len(completed_todos)}/{len(emp_todos)}):')
    for todo in completed_todos:
        print(f'\t {todo.get("title")}')
