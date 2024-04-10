#!/usr/bin/python3
"""
    function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
        function that queries the Reddit API and prints
        the titles of the first 10 hot posts
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts:
            for post in posts:
                print(post['data']['title'])
        else:
            print("No posts found.")
    else:
        print("None")
