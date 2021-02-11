import boto3


def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    table = client.Table("commands")

    response = table.scan(AttributesToGet=['key'])

    for i in response['Items']:
        table.delete_item(Key={
            'key': i['key']
        }
        )
    return {"statusCode": 200, "body": "OK"}
