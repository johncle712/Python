import boto3

s3_resource = boto3.client("s3")
list_bucket = s3_resource.list_buckets()

for bucket in list_bucket["Buckets"]:
    print(bucket["Name"]) 
    print(bucket["CreationDate"],"\n")