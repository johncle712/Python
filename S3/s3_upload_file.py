import resource
import boto3

s3=boto3.client('s3')

#upload single file
s3.upload_file(
    Filename="/Users/johnle/Desktop/test.jpg",
    Bucket="boto3-luit-jl7392384",
    Key="test.jpg"
)

#upload multiple files

import os
import glob

cwd=os.getcwd()
cwd=cwd+"/upload/"
files=glob.glob(cwd+"*.jpg")

for file in files:
    s3=boto3.client('s3')
    s3.upload_file(
    Filename=file,
    Bucket="boto3-luit-jl7392384",
    Key=file.split("/")[-1]
    )