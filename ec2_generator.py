#EC2 random name generation for week 13 in LUIT

import string
import random

#Only these departments are authorized to use this application.
authorized_dept = ["marketing", "accounting", "finops"]

print ("This program will generate a random name for your EC2 instances\n")

#Ask user for input and convert to lower
dept_name = input("Please enter the department that you work in:\n").lower() 

#Logic for verifying use is in correct group
if dept_name in authorized_dept:
    ec2_inst = input("How many EC2 instances would you like to create?:\n")
    
else:
    print("Your department is not authorized to use this program!!")
    exit()

#input validation to confirm user entered a number
if not ec2_inst.isdigit():
    print("Enter valid number!")
    exit()

#If user prints enters a digit, display send welcome message with number of instances
if ec2_inst.isdigit():
    print("Hello", dept_name, "Department!", "I see you would like to create", ec2_inst, "instances.\n")
    ec2_inst= int(ec2_inst)

#Used to generate random 10 character and intergers
random_chars = "".join(random.choices(string.ascii_letters+string.digits, k=10))

#loop to concatenate department name and random characters
for _ in range(ec2_inst):
    print("Here is your randomly generated name based on your dept:")
    print((dept_name + "-" + random_chars),"\n")