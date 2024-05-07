#!/usr/bin/python3
"""
Function to query the Reddit API and print the titles of the first 10 hot.
"""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=10"
    headers = {"User-Agent": "Holberton"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("None")
        return

    data = response.json().get("data")
    children = data.get("children")
    if children:
        for child in children:
            print(child.get("data").get("title"))
    else:
        print("None")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
