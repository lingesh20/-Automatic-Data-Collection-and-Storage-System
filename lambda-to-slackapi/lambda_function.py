import os
import json
import requests

def lambda_handler(event, context):
    # Check if the event indicates that the alarm has been triggered
    if event.get('alarm_triggered'):
        # Send a message to the Slack channel
        message = event.get('message', 'No message provided')
        send_slack_message(message)
        # send_slack_message("Data successfully inserted in ")
        
    return {
        'statusCode': 200,
        'body': json.dumps('Message sent to Slack!')
    }

def send_slack_message(message):
    slack_token = os.environ["slack_token"]
    slack_channel = "C06STLJV7S5"  # Replace with your Slack channel name or ID
    slack_url = f"https://hooks.slack.com/services/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"
    # slack_url = f"https://hooks.slack.com/services/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"
    
    headers = {
        "Authorization": f"Bearer {slack_token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "channel": slack_channel,
        "text": message
    }
    
    response = requests.post(slack_url, headers=headers, json=payload)
    
    if response.status_code != 200:
        print(f"Failed to send message to Slack: {response.text}")
    else:
        print("Message sent successfully to Slack!")
