#read list
fruit = ["apples","oranges","bananas"]
print(fruit[1])

#print length of fruit
print (len(fruit))

#append kiwi
fruit.append("kiwi")
print(fruit)
['apples', 'oranges', 'bananas', 'kiwi']

#insert passion fruit to index 2
fruit.insert(2, "passion fruit")
print(fruit)
['apples', 'oranges', 'passion fruit', 'bananas', 'kiwi']

#sort list
print(sorted(fruit))
['apples', 'bananas', 'kiwi', 'oranges', 'passion fruit']
print(fruit)
['apples', 'oranges', 'passion fruit', 'bananas', 'kiwi']

#Delete fruit
favorite_fruit = fruit.pop()
print(favorite_fruit)

fruit.remove('bananas')
print(fruit)
['passion fruit']
