#!/usr/bin/python3

"""
This script fetches TODO list progress for a given employee ID using a REST API.
It accepts an integer as a parameter, which is the employee ID.
It displays the employee TODO list progress in a specific format and exports the data in CSV format.
"""

import requests
import csv
import sys

def fetch_todo_list_progress(employee_id):
    """
    Fetches TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: List of dictionaries containing task information.
    """
    # API endpoint
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetching data from the API
    response = requests.get(url)
    todos = response.json()

    return todos

def export_to_csv(employee_id, todos):
    """
    Exports TODO list progress to a CSV file.

    Args:
        employee_id (int): The ID of the employee.
        todos (list): List of dictionaries containing task information.

    Returns:
        None
    """
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for todo in todos:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': todo.get('name'),
                'TASK_COMPLETED_STATUS': todo.get('completed'),
                'TASK_TITLE': todo.get('title')
            })

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    todos = fetch_todo_list_progress(employee_id)
    export_to_csv(employee_id, todos)
