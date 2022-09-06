import boto3

ec2=boto3.client("ec2")

ec2.delete_snapshot(SnapshotId='snap-06d107f9141863d56')