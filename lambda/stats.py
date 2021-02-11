from collections import Counter
import json
import boto3


def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    table = client.Table("commands")

    response = table.scan(AttributesToGet=['command'])
    lst = []
    for i in response['Items']:
        lst.append(i['command'])
    er = Counter(lst)
    return {"statusCode": 200, "body": json.dumps(er)}

