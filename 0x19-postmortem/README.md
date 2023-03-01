
stmortem



Issue Summary 
A WordPress website was down for 30 minutes, from 10:00am to 10:30am (UTC+1) on August 15th 2020. This caused the website to be inaccessible for the users, and all the services that relied on it were also affected. The root cause of the issue was an incorrect extension of a file in the WordPress installation. 

Timeline 
10:00am - The issue was detected after a customer complained about being unable to access the website. 
10:15am - After initial investigation, it was determined that the issue was related to the WordPress installation. 
10:20am - After further investigation, it was determined that a file in the WordPress installation had an incorrect extension, which was causing the issue. 
10:25am - The issue was fixed by using a sed command to update the incorrect extension. 
10:30am - The website was back up and functioning as expected. 

Root Cause and Resolution 
The root cause of the issue was 

An incorrect extension of a file in the WordPress installation. 
The file in question was wp-settings.php,
 which had an incorrect extension of “phpp” instead of “php”. 
To fix the issue, the sed command was used to update the incorrect extension, which resulted in the website being back up and functioning as expected. 

Corrective and Preventative Measures 
To prevent this issue from occurring in the future, the following steps can be taken: 

Review the WordPress installation regularly to ensure that all files have the correct extensions. 
Set up monitoring to detect any changes in the WordPress installation. 
Create backups of the WordPress installation on a regular basis. 
Set up automated tests to detect any issues or changes in the 
WordPress installation.

