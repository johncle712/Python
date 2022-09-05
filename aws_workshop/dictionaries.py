#Create a value
user = {"first_name":"Ada"}
print(user)
{'first_name': 'Ada'}

#read
user = {"first_name":"Ada"}
print(user["first_name"])

#add a key-value
user["family_name"] = "Byron"
print(user)
{'first_name': 'Ada', 'family_name': 'Byron'}

#modify a value
user["family_name"] = "Lovelace"
print(user)
{'first_name': 'Ada', 'family_name': 'Lovelace'}

#Delete a key value pair
del user["family_name"]
print(user)
{'first_name': 'Ada'}
