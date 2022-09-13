import json
import boto3
import random
import string


def lambda_handler(event, context):
    
    sqs = boto3.client('sqs')
    
    random_num_str = (''.join(random.choices(string.ascii_letters+string.digits, k=10)))
    hello_message = ('Hello this is a random number and string of: ')
    
    response = sqs.send_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/548749819847/week-15-queue',
        MessageBody=(hello_message+random_num_str))
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
