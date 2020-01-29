# equals: a == b
# not equals: a != b
# less than: a < b
# less than or equal to: a <= b
# greater than: a > b
# greater than or equal to: a >= b

# if statement

a = 24
b = 25

if b > a:
    print ("b is greater than a")
# print ("b is greater than a") = error

# elif -> if the previous condition was not true, then try this condition

c = 32
d = 32

if c > d:
    print ("c is greater than d")
elif c == d:
    print ("c and d are equal")

# else -> catches anything which is not caught by the preceding conditions.

a = 200
b = 33

if b > a:
    print ("b is greater than a")
elif a == b:
    print ("a and b are equal")
else:
    print ("a is greater than b")

# short hand if -> one statement to execute

if a > b: print ("a is greater than b")

# short hand if...else -> one statement to execute, one for if, and one for else

a = 2
b = 330

print("A") if a > b else print ("B")

# and -> logical operator, used to combine conditional statements

a = 200
b = 33
c = 500

if a > b and c > a:
    print ("Both condition are True")


# or -> same as and

a = 200
b = 33
c = 500

if a > b or a > c:
    print ("At least one of conditions is True")


# nested if -> if statement inside if statement

x = 41

if x > 10:
    print ("Above ten")
    if x > 20:
        print ("and also above 20!")
    else:
        print ("but not above 20.")


# pass statement -> if cannot be empty, use pass to avoid error

a = 33
b = 200

if b > a:
    pass