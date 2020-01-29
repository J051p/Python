# A for loop is used for iterating over a sequence (a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and work more like an iterator
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Looping through a string

for x in "banana":
    print(x)

# The break statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break # exit loop when x is banana

# exit the loop when x is "banana", but this time the break comes before the print

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
    print(x)

# The continue statement, we can stop the current iteration of the loop, and continue with the next

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana": # do not print "banana"
        continue
    print(x)

# The range() function -> looping through a set of code a specified number of times
# Returns a sequence of numbers, starting from 0 by default, and increments by 1 by default

for x in range(10):
    print(x)

# specific range

for x in range(3, 8):
    print(x)

# increment the sequence with 2

for x in range(3, 30, 3): # plus 3 from 3
    print(x)


# else in for loop
# print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
    print(x)
else:
    print("Finally finished!")


# nested loops
# loop inside a loop, inner loop will be executed one time for each iteration of outer loop

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# the pass statement
# for loops cannot be empty, but putting pass statement can avoid getting an error

for x in [0,1,2]:
    pass 