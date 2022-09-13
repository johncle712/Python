import boto3

sqs = boto3.resource('sqs')

queue = sqs.create_queue(
    QueueName='week-15-queue',
)

sqs_queue = boto3.client('sqs')

response = sqs_queue.get_queue_url(QueueName='week-15-queue')

print(response['QueueUrl'])