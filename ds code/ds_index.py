# data strucrures
# 1. list
# list is ordered collection of items
# list is mutable
# list is used when we want to store multiple items in a single variable
# list is represented by square brackets
# list is index based collection of items
# list supports slicing
# list supports negative indexing
# list supports nested list

food = ['dahi balle', 'biryani', 'shammi', ' palak paaneer', 'samose']
print(type(food))
print(food)
print(food[3])
food[1]='chicken palao'
print(food)

#TUPLE
# tuple is immutable
# tuple is faster than list
# tuple is used when we don't want to change the data
tup = ('dahi balle', 'biryani', 'shammi', 'palak paaneer', 'samose')

print(type(tup))
print(tup)
print(tup[3])
#tup[1]='chicken palao' ERROR, AS TUPLE IS IMMUTABLE
print(tup)

#SET
# set is unordered collection of unique items
# set is used when we want to remove duplicates
# set is faster than list and tuple
# EXAMPLE SETS TO REMOVE DUPLICATES
s = {10, 20, 30, 40, 50, 10, 20, 30, 40}
print(s)

#DICTIONARY
# dictionary is key-value pair
# dictionary is unordered collection of items
# dictionary is mutable
# dictionary is used when we want to store data in key-value pair
# dictionary is represented by curly brackets
# dictionary is accessed by key
# dictionary supports nested dictionary
# dictionary supports nested list
# dictionary supports nested tuple
# dictionary supports nested set
d = {'name':'Rahul', 'age':25, 'city':'delhi', 'marks':[90, 80, 70]}
print(d)






