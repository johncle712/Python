import boto3

client=boto3.client("ec2")
client.delete_vpc(
    VpcId='vpc-042ca7758805d9e19'
)