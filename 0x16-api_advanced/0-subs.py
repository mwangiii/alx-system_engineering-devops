#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" query reddit API and return number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """ return number of subscribers """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'This Agent?'}
    r = requests.get(url, headers=headers)
    if r.status_code == 404:
        return 0
    return r.json().get('data').get('subscribers')


if __name__ == '__main__':
    number_of_subscribers(subreddit)
