import json
import boto3

S3_DEST_KEY = 'cloudfront/widgets-events-json/file1.txt'
s3 = boto3.client('s3')

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    _write_to_s3('newscred-serverless-dev-test-bucket', S3_DEST_KEY)
    return response

def _write_to_s3(bucket, dest_key):
    s3.put_object(Bucket=bucket, Key=dest_key, Body='hello')