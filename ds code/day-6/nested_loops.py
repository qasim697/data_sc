#some  useful examples of nested loops
#1. printing a table
for i in range(1, 11):
      for j in range(1, 11):
            print(f"{i} * {j} = {i*j}", end="\t")
            print() #this will print a new line after each row
            
#2. printing a matrix
matrix = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
for row in matrix:
      for element in row:
            print(element, end="\t")
            print() #this will print a new line after each row
                  
            

