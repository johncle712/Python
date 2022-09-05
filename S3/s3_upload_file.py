import resource
import boto3

s3=boto3.client('s3')

#upload single file
s3.upload_file(
    Filename="/Users/johnle/Desktop/test.jpg",
    Bucket="boto3-luit-jl7392384",
    Key="test.jpg"
)



