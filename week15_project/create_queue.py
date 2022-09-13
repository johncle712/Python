import boto3

sqs = boto3.resource('sqs')

#create queue
queue = sqs.create_queue(
    QueueName='week-15-queue',
)

sqs_queue = boto3.client('sqs')

#grabs the url from our queue name
response = sqs_queue.get_queue_url(QueueName='week-15-queue')

#prints our url
print(response['QueueUrl'])