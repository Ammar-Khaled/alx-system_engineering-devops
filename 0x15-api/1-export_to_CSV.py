#!/usr/bin/python3
"""
This module uses the "JSONPlaceholder" REST API
for a given employee ID accepted as an integer argument
and saves information about his/her TODO list progress in a csv file.
"""


if __name__ == "__main__":
    import csv
    from requests import get
    from sys import argv

    url = 'https://jsonplaceholder.typicode.com/'
    emp_id = argv[1]
    saving_file = f'{emp_id}.csv'

    response = get(url + f'users/{emp_id}')
    emp_username = response.json().get('username')

    response = get(url + f'users/{emp_id}/todos')
    emp_todos = response.json()

    with open(saving_file, 'w', newline='') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        rows = []
        for todo in emp_todos:
            rows.append([emp_id, emp_username,
                         todo.get('completed'), todo.get('title')])

        csv_writer.writerows(rows)
