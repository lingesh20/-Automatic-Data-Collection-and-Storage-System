import os
import json
import requests

def lambda_handler(event, context):
    # Check if the event indicates that the alarm has been triggered
    if event.get('alarm_triggered'):
        # Send a message to the Slack channel
        send_slack_message("Alarm triggered! Take action.")
        
    return {
        'statusCode': 200,
        'body': json.dumps('Message sent to Slack!')
    }

def send_slack_message(message):
    slack_token = os.environ["slack_token"]
    slack_channel = "C06STLJV7S5"  # Replace with your Slack channel name or ID
    slack_url = f"https://hooks.slack.com/services/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"
    
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
