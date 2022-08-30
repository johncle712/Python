#Several departments share an AWS environment. You need to ensure that the EC2s are properly named 
#and are unique so team members can easily tell who the EC2 instances belong to. Use Python to 
#create your unique EC2 names that the users can then attach to the instances. The Python Script 
#should:

#1. All the user to input how many EC2 instances they want names for and output the same amount of unique names.
#2. Allow the user to input the name of their department that is used in the unique name.
#3. Generate random characters and numbers that will be included in the unique name.

import string
import random

authorized_dept = ["marketing", "accounting", "finops"]

print ("This program will generate a random name for your EC2 instances\n")

ec2_inst = input("How many EC2 instances would you like to create?:\n")

dept_name = input("Please enter the department that you work in:\n").lower()

if dept_name in authorized_dept:
    print("Great! Your department is not authorized to use this program!!")
else:
    print("You are not authorized to use this program!")
    exit()


print ("hello !", dept_name)

