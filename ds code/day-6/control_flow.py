# control flow statements in python
# if-else statements
a=20
b=30
if a>b:
    print('a is greater than b')
else:
      print('b is greater than a')
      # output: b is greater than a
      
# if-elif-else statements


# for loops example
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)
# output: apple
# example of for loop with range
for i in range(5):
      print(i)
      # output: 0,1,2,3,4
      
# example of for loop with range and step
for i in range(0, 10, 2):
      print(i)
      # output: 0,2,4,6,8
      
# example of for loop with range and negative step
for i in range(10, 0, -2):
      print(i)
      # output: 10,8,6,4,2
      


# while loops example
i = 1
while i < 6:
      print(i)
      i += 1
      # output: 1,2,3,4,5
# example of while loop with break statement
i = 1
while i < 6:
      print(i)
      if i == 3:
            break
      i += 1
      # output: 1,2,3
# example of while loop with continue statement
i = 0
# while i < 6:
#       if i == 3:
#             continue
#       print(i)
#       i += 1
      
      # output: 0,1,2,4,5
# example of while loop with pass statement
i = 0
while i < 6:
      if i == 3:
            pass
      print(i)
      i += 1
      # output: 0,1,2,3,4,5
      


# using nested loops, print stars  in a triangle shape
i=0
for i in range(5):
      for j in range(i):
            print("*", end=" ")
            

