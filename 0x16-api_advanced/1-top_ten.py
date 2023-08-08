#!/usr/bin/python3
"""
Script that prints out top ten hottest gists
of a subreddit
"""

import requests


def top_ten(subreddit):
    """Function that fetches top 10 gists"""
    apiUrl = f"https://www.reddit.com/r/{subreddit}/hot.json"
    userAgent = "Mozilla/5.0"
    limits = 10

    response = requests.get(
        apiUrl, headers={"user-agent": userAgent}, params={"limit": limits})
    if response.status_code != 200:
        print("None")
        return
    response_data = response.json()
    list_obj = response_data['data']['children']
    for obj in list_obj:
        print(obj['data']['title'])


if __name__ == "__main__":
    subreddit_name = input("Enter the subreddit name: ")
    top_ten(subreddit_name)
