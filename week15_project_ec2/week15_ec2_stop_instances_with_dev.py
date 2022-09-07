import boto3

ec2 = boto3.client('ec2')

#Looks for envirnoment tag with value dev
tags={'Name': 'tag:environment','Values': ['dev']}

#Looks for instances that is running
running={'Name': 'instance-state-name', 'Values': ['running']}

#iterate through all instances with tags and running state
for each_instance in ec2.describe_instances(Filters=[tags,running])['Reservations']:
    for inst_id in each_instance['Instances']: # grab each instance and store in inst_id
        ec2.stop_instances(InstanceIds=[inst_id['InstanceId']]) #stop instances from dictionary list of inst_id
        print("The following instances are stopping: ", [inst_id['InstanceId']])
