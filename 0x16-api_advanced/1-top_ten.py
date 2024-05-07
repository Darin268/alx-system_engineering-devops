#!/usr/bin/python3
"""
This module contains the function top_ten.
"""
import requests
import sys


def top_ten(subreddit):
    """
    Returns the top ten posts for a given subreddit.
    """
    user_agent = {'User-Agent': 'Lizzie'}
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    response = requests.get(url, headers=user_agent)

    try:
        data = response.json().get('data', {}).get('children', [])
        for post in data:
            print(post.get('data', {}).get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <subreddit>".format(sys.argv[0]))
        sys.exit(1)
    top_ten(sys.argv[1])
