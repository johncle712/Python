import boto3

aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("boto3-luit-jl7392384")

response = bucket.create(
    ACL= 'public-read',
)

print(response)