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
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Python/1.0(Holberton School 0x16 task 0)'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            return data.get('subscribers', 0)
        else:
            return 0
    except Exception as e:
        return 0
