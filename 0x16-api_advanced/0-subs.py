#!/usr/bin/python3
def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers 
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    import requests
    
    # Set custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Reddit Subscriber Checker'}
    
    # Make the request
    response = requests.get('https://www.reddit.com/r/' + subreddit + '/about.json', headers=headers)
    
    # Check if subreddit is valid
    if response.status_code == 200:
        # Parse json data
        data = response.json()
        # Return the number of subscribers
        return data['data']['subscribers']
    else:
        # If invalid subreddit, return 0
        return 0
