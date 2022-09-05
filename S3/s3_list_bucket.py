import boto3

resource=boto3.resource("s3")
bucket_list = list(resource.buckets.all())

#print length of buckets
print (len(bucket_list))

#print out all buckets
for bucket in resource.buckets.all():
    print(bucket.name)