<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>README.md</title>
  <style>
    table, td, th{
      border: 1px solid black;
      border-collapse: collapse;
    }
  
  </style>
</head>
<body>
  <h1>README.md 0x16. API advanced</h1>

<p>This repository contains the solutions to the tasks in the 0x16-api_advanced project of the ALX System Engineering & DevOps program.
The tasks in this project involve using the Reddit API to query for information about subreddits and their posts. The project uses the Requests module to send HTTP requests to the Reddit API.</p><br>
<p>The following tasks are completed in this project:</p>
<ol><li>How many subs?</li>
  <ul>
    <li>Write a function that queries the Reddit API for the number of subscribers to a given subreddit.</li>
    <li>If the subreddit is invalid, return 0.</li>
    <li>Ensure that the function does not follow redirects to search results.
</li>
  </ul>
<li>Top Ten</li>
<ul>
  <li>Write a function that queries the Reddit API for the first 10 hot posts in a given subreddit.</li>
  <li>If the subreddit is invalid, print None.</li>
  <li>Ensure that the function does not follow redirects to search results.</li>
</ul>
  
<li>Recurse it!</li>
<ul>
  <li>Write a recursive function that queries the Reddit API for all hot articles in a given subreddit.</li>
  <li>The function must return a list of the titles of the articles.</li>
  <li>If the subreddit is invalid, the function must return None.
</li>
</ul>
<li>Count it!</li>
<ul>
  <li>Write a recursive function that queries the Reddit API for all hot articles in a given subreddit.</li>
  <li>The function must parse the titles of the articles and count the number of occurrences of each keyword.</li>
  <li>The function must print the keywords in descending order by the number of occurrences, with ties broken alphabetically</li>
</ul></ol><br>
<h2>Getting Started</h2>
<p>To get started with this project, you will need to have the following installed:</p>
<ul>
  <li>Python 3</li>
  <li>The Requests module</li>
</ul>

<p>Once you have these installed, you can clone the GitHub repository for this project:</p><br>
<p>git clone https://https://github.com/ben11997/alx-system_engineering-devops.git/</p>
<h3>Usage</h3>
<p>To use the code in this project, you will need to edit the config.py file to provide your Reddit API credentials. Once you have done this, you can run the following commands to execute the tasks in the project:</p>
  
  <table>
    <tr>
      <th>FILE</th>
      <th>FUNCTION</th>
    </tr>
    <tr>
      <td>0-subs.py</td>
      <td>def number_of_subscribers(subreddit)</td>
    </tr>
    <tr>
      <td>1-top_ten.py</td>
      <td>def top_ten(subreddit) </td>
    </tr>
    <tr>
      <td>100-count.py</td>
      <td>def count_words(subreddit, word_list</td>
    </tr>
  </table>

<p>For example, to run the top_ten task for the programming subreddit, you would run the following command:
python3 1-main.py programming</p>

<p><em><h3>Author</h3></em> Abraham Benson.</p>

</body>
</html>
