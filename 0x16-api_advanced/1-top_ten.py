#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Module to print the top 10 hot posts of a subreddit"""

import requests


def top_ten(subreddit):
    """Function to print the top 10 hot posts of a subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        for post in response.json().get('data').get('children'):
            print(post.get('data').get('title'))
    else:
        print(None)


if __name__ == '__main__':
    top_ten(input('Subreddit: '))
