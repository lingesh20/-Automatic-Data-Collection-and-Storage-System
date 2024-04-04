import json
import pymysql
import requests
import datetime
import boto3

rds_host = "database-1.cjka0akmyk2t.ap-south-1.rds.amazonaws.com"
username = "admin"
password = "admin123"
db_name = "finalproject"


def lambda_handler(event, context):
    try:
        # API endpoint to fetch JSON data
        api_url = "http://api.open-notify.org/iss-now.json"
        
        # Fetch data from the API
        response = requests.get(api_url)
        data = response.json()
        
        time_stamp = data['timestamp']
        datetime_object = datetime.datetime.fromtimestamp(time_stamp)
        latitude = data['iss_position']['latitude']
        longitude = data['iss_position']['longitude']
        
        # Connect to the RDS database
        conn = pymysql.connect(host=rds_host, user=username, password=password, database=db_name)
        cursor = conn.cursor()
        
        # Create a table if not exists
        create_table_query = """
        CREATE TABLE IF NOT EXISTS api_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            timestamp DATETIME,
            latitude DECIMAL(10, 7),
            longitude DECIMAL(10, 7)
        )
        """
        cursor.execute(create_table_query)
        
        # Insert data into the database
        insert_query = "INSERT INTO api_data (timestamp,latitude,longitude) VALUES (%s,%s,%s)"
        cursor.execute(insert_query, (datetime_object, latitude, longitude))
        
        # Commit the transaction
        conn.commit()
        
        # Close the database connection
        cursor.close()
        conn.close()
        
        invoke_another_lambda()
        
        return {
            'statusCode': 200,
            'body': json.dumps('Data inserted successfully into RDS')
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Error inserting data into RDS: {}'.format(str(e)))
        }
        
def invoke_another_lambda():
    # Create Lambda client
    try:
        # Create Lambda client
        lambda_client = boto3.client('lambda')

        # Specify the ARN of the Lambda function you want to invoke
        target_lambda_arn = 'arn:aws:lambda:ap-south-1:730335666642:function:stackapi'

        # Construct payload if needed
        payload = {
            "alarm_triggered": True
        }

        # Invoke the Lambda function
        response = lambda_client.invoke(
            FunctionName=target_lambda_arn,
            InvocationType='Event',  # Asynchronous invocation
            Payload=json.dumps(payload) if payload else None
        )

        # Optionally, you can handle the response
        # print(response)
    except Exception as e:
        print("Error invoking lambda: ", str(e))