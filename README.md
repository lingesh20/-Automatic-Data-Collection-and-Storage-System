# -Automatic-Data-Collection-and-Storage-System

Introduction:

This project involves creating Automated Server Monitoring and Notification System powered by AWS Lambda and Slack Integration. This system ensures continuous server availability by fetching data from an API, storing it in Amazon RDS, and promptly alerting via Slack in case of downtime. With seamless integration and automated execution, it offers proactive server management for uninterrupted service delivery.

Technologies Used:

* Python scripting
* AWS Lambda
* Amazon RDS
* CloudWatch
* Data Management using MongoDB and SQL
* Slack API


The result of the above approach would be an AWS Lambda function that is continuously running and performing the following tasks: 
·  Fetching data from an API on a regular basis (every 15 seconds).
·  Storing the fetched data in an Amazon RDS database.
·  Monitoring the server's availability using a CloudWatch Alarm.
·  Sending a notification to a Slack channel if the server becomes unavailable.
