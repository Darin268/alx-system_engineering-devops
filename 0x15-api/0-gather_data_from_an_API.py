#!/usr/bin/python3

"""
This script fetches TODO list progress for a given employee ID using a REST API.
It accepts an integer as a parameter, which is the employee ID.
It displays the employee TODO list progress in a specific format.
"""

import requests
import sys

def fetch_todo_list_progress(employee_id):
    """
    Fetches TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # API endpoint
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetching data from the API
    response = requests.get(url)
    todos = response.json()

    # Filtering completed tasks
    completed_tasks = [todo for todo in todos if todo.get('completed')]

    # Displaying progress
    employee_name = todos[0].get('name')
    total_tasks = len(todos)
    completed_count = len(completed_tasks)
    print(f"Employee {employee_name} is done with tasks ({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    fetch_todo_list_progress(employee_id)
