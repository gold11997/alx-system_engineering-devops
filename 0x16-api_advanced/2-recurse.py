
#!/usr/bin/python3
def recurse(subreddit, hot_list=[]):
    """
    Queries the Reddit API and returns a list containing the titles of all 
    hot articles for a given subreddit. If no results are found for the 
    given subreddit, the function should return None.
    """
    import requests
    
    # Set custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Reddit Article Title Checker'}
    
    # Make the request
    response = requests.get('https://www.reddit.com/r/' + subreddit + '/hot.json', headers=headers)
    
    # Check if subreddit is valid
    if response.status_code == 200:
        # Parse json data
        data = response.json()
        # Append titles to hot_list
        for article in data['data']['children']:
            hot_list.append(article['data']['title'])
        # Check if there are more pages
        if data['data']['after'] is not None:
