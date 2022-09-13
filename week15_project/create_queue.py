import boto3

sqs = boto3.resource('sqs')

queue = sqs.create_queue(
    QueueName='week-15-queue',
)

print(queue.url)
