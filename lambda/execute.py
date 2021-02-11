import json
import subprocess
import boto3
import uuid


def lambda_handler(event, context):
    event_body = json.loads(event['body'])

    command = event_body['command']
    client = boto3.resource('dynamodb')
    table = client.Table("commands")

    table.put_item(Item={'key': uuid.uuid4().hex, 'command': command})
    stdout = subprocess.check_output(command, shell=True)

    return {
        'statusCode': 200,
        'body': stdout
    }
