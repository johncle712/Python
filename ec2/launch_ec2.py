from urllib import response
import boto3

ec2=boto3.resource("ec2")
ec2.create_instances(
    ImageId='ami-05fa00d4c63e32376',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
)