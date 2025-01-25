# functions in python
def greet(name):
      return "Hello, " + name + "!"
print(greet("John"))
# output: Hello, John!

def aoa(name="qasim"):
      print(f"salamoalaikum!{name} all the way from london")
aoa()

name = input("Enter your n name:")

print(greet(name))
aoa(name)

def square(x):
      return x*x

print(square(5))
# output: 25
# functions in pythonazam


# recursion 
def factorial(n):
      if n == 0:
            return 1
      else:
            return n * factorial(n-1)
print(factorial(1))

# lambda function
# lambda arguments: expression
x = lambda a : a + 10
print(x(5))

# two parameters
x = lambda a, b : a * b
print(x(5, 6))
