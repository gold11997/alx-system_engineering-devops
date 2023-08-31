#!/usr/bin/python3
"""
Using reddit's API
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
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
                sorted_words = sorted(word_count.items(),
                                      key=lambda x: (-x[1], x[0]))
                for word, count in sorted_words:
                    print(f"{word}: {count}")
                return
            for child in children:
                title = child.get("data", {}).get("title", "").lower()
                for word in word_list:
                    if title.count(word) > 0:
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1
            after = data.get("after")
            return count_words(subreddit, word_list, after, word_count)


if __name__ == "__main__":
    subreddit_name = "your_subreddit_here"
    keywords = ["keyword1", "keyword2", "keyword3"]  # Add your keywords here
    count_words(subreddit_name, keywords)
