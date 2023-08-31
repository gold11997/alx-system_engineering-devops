#!/usr/bin/python3

"""
Using reddit's API
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after}

    response = requests.get(url, params=params,
                            headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        if data and "children" in data:
            children = data["children"]
            if not children:
                return hot_list
            for child in children:
                title = child.get("data", {}).get("title")
                if title:
                    hot_list.append(title)
            after = data.get("after")
            return recurse(subreddit, hot_list, after)
    return None


subreddit_name = "your_subreddit_here"
hot_titles = recurse(subreddit_name)

if hot_titles is None:
    print("Invalid subreddit or no results found.")
else:
    for i, title in enumerate(hot_titles, start=1):
        print(f"{i}. {title}")

