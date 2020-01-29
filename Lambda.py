#  A lambda function is small anonymous function. It can take any number of arguments, but can only have one expression.

x = lambda a : a + 10 # adds 10 to the number passed in as an argument.
print(x(5))

x = lambda b : b * 3
print(x(5))

x = lambda a, b : a * b
print(x(8, 7)) # 56

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Use lambda inside another function.