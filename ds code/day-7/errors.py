#types of errors in python
# 1. Syntax Error
# 2. Logical Error
# 3. Runtime Error
# 4. Exceptions
# 1. Syntax Error
# This occurs when the code is not written correctly according to the Python syntax rules.
# Example:
# print("Hello World"  # Missing closing parenthesis

# 2. Logical Error
# This occurs when the code runs without crashing but produces incorrect results.
# Example:
def add(a, b):
      return a - b  # Logical error: should be a + b

result = add(5, 3)
print(result)  # Output will be 2 instead of 8

# 3. Runtime Error
# This occurs during the execution of the program and causes it to crash.
# Example:
# print(10 / 0)  # Division by zero error

# 4. Exceptions
# These are errors that can be caught and handled using try-except blocks.
# Example:
try:
      print(10 / 0)
except ZeroDivisionError as e:
      print(f"Caught an exception: {e}")