#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys

def get_employee_info(employee_id):
    try:
        base_url = "https://jsonplaceholder.typicode.com/users"
        employee_url = f"{base_url}/{employee_id}"

        response = requests.get(employee_url)
        response.raise_for_status()
        employee_data = response.json()
        employee_name = employee_data.get('name')

        todo_url = f"{employee_url}/todos"
        response = requests.get(todo_url)
        response.raise_for_status()
        tasks = response.json()

        done_tasks = [task for task in tasks if task.get('completed')]
        done = len(done_tasks)
        total_tasks = len(tasks)

        print(f"Employee {employee_name} is done with tasks({done}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t{task.get('title')}")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_info(employee_id)

