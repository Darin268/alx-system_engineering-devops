#!/usr/bin/python3
"""Function to query the Reddit API and print the titles of the first 10 hot posts for a given subreddit."""

import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data")
    if not data:
        print(None)
        return

    children = data.get("children")
    if not children:
        print(None)
        return

    for post in children:
        print(post.get("data").get("title"))


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
