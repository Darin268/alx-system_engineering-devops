#!/usr/bin/python3
"""
Script to fetch task data for all employees from an API and export it in JSON format.
"""

import json
import requests
import sys

def fetch_tasks():
    """
    Fetches task data for all employees from an API.
    Returns:
        dict: Dictionary containing tasks for all employees.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = response.json()
    
    all_employees_tasks = {}
    
    for todo in todos:
        user_id = str(todo["userId"])
        task_data = {
            "username": todo["username"],
            "task": todo["title"],
            "completed": todo["completed"]
        }
        all_employees_tasks.setdefault(user_id, []).append(task_data)
    
    return all_employees_tasks

def export_to_json(data, filename):
    """
    Exports data to a JSON file.
    Args:
        data (dict): Data to export.
        filename (str): Name of the JSON file.
    """
    with open(filename, "w") as json_file:
        json.dump(data, json_file)

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python3 script_name.py")
        sys.exit(1)

    tasks_data = fetch_tasks()
    export_to_json(tasks_data, "todo_all_employees.json")
