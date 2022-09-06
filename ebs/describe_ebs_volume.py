import boto3

ec2=boto3.client("ec2")

ec2.describe_snapshots(SnapshotIds=['snap-072a5259501813ed9'])