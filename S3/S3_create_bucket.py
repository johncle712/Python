import boto3

aws_resource = boto3.resource ("S3")
bucket = aws_resource.bucket ("boto3_LUIT")

response = bucket.create(
    ACL= 'public-read'
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-1'
    },
)