#!/usr/bin/python3
""" Query Reddit API to determine subreddit sub count"""

import requests

def count_words(subreddit, word_list, count_list=None, next_page=None):
    """Request subreddit recursively using pagination"""
    if count_list is None:
        count_list = [{'keyword': word, 'count': 0} for word in word_list]

    user_agent = '0x16-api_advanced-jmajetich'
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    if next_page:
        url += f'{"?" if "?" not in url else "&"}after={next_page}'

    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return

    data = r.json()['data']

    posts = data['children']
    for post in posts:
        title = post['data']['title']
        for item in count_list:
            title_lower = title.lower()
            title_list = title_lower.split()
            item['count'] += title_list.count(item['keyword'].lower())

    next_page = data['after']
    if next_page is not None:
        return count_words(subreddit, word_list, count_list, next_page)
    else:
        sorted_list = sorted(count_list,
                             key=lambda word: (word['count'], word['keyword']),
                             reverse=True)
        keywords_matched = 0
        for word in sorted_list:
            if word['count'] > 0:
                print(f'{word["keyword"]}: {word["count"]}')
                keywords_matched += 1
        return
