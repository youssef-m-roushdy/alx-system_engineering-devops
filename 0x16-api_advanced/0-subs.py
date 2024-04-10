#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of total subscribers for a given
subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of total subscribers for a
    given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'my-custom-user-agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
