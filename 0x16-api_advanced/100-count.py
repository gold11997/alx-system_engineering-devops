#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests

def count_words(subreddit, word_list):

    # Set up necessary variables
    import requests
    import json
    from collections import Counter
    result_count = Counter()
    after = None
    
    # Create a request to the Reddit API to get the hot posts from the specified subreddit
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 100}
    if after:
        params['after'] = after
    res = requests.get(url, params=params, headers={'User-agent': 'Mozilla/5.0'})
    
    # If the subreddit is invalid, return nothing
    if res.status_code == 200:
        json_data = json.loads(res.content)
        children = json_data['data']['children']
        after = json_data['data']['after']
        
        # Loop through each post in the response
        for post in children:
            title = post['data']['title'].lower()
            title_words = title.split()
            
            # Iterate through word_list to find matching words
            for word in word_list:
                word_count = title_words.count(word.lower())
                result_count[word.lower()] += word_count
                
        # Make a recursive call with the after parameter if there are more posts
        if after:
            count_words(subreddit, word_list)
            
    # Print the results in descending order
    for word in sorted(result_count, key=result_count.get, reverse=True):
        if result_count[word] > 0:
            print('{}: {}'.format(word, result_count[word]))
