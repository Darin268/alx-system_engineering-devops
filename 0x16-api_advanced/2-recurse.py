#!/usr/bin/python3
"""
Recursive function to query Reddit API for hot articles in a subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of titles of all hot articles for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "Holberton"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    after = data.get("after")
    children = data.get("children")
    if children:
        for child in children:
            hot_list.append(child.get("data").get("title"))
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result:
            print(len(result))
        else:
            print("None")
