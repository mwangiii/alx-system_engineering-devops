#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" return list containing the titles of\
    all hot articles for a given subreddit """

import requests


def recurse(subreddit, hot_list=[], after=None):
    """ return list containing the titles of\
        all hot articles for a given subreddit """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
        after = data.get('after')
        children = data.get('children')
        for child in children:
            hot_list.append(child.get('data').get('title'))
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None


if __name__ == '__main__':
    recurse(subreddit)
