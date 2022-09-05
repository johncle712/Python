from urllib import response
import boto3

#Delete single object
s3=boto3.client("s3")
objects=s3.delete_object(Bucket="boto3-luit-jl7392384",Key="test5.jpg")

#delete multiple objects
import os
import glob

objects=s3.list_objects(Bucket="boto3-luit-jl7392384")["Contents"]

for object in objects:
    s3.delete_object(Bucket="boto3-luit-jl7392384",Key=object["Key"])
    print(response)