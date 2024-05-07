#!/usr/bin/python3
"""Recursive function to query the Reddit API and return a list of titles of all hot articles for a given subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively query the Reddit API and return a list of titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): The list to store the titles of hot articles.
        after (str): The parameter to paginate through results.

    Returns:
        list: A list containing the titles of all hot articles for the subreddit, or None if no results are found.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json().get("data")
    if not data:
        return hot_list

    children = data.get("children")
    if not children:
        return hot_list

    for post in children:
        hot_list.append(post.get("data").get("title"))

    after = data.get("after")
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
