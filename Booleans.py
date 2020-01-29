# True or False

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 24
b = 24.5

if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

# Evaluate values and variables

print(bool("Pozz"))
print(bool(24))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Most values are True, if it has some content, any string is true, except empty string, any number except 0, any list,tuple,set and dictionary are True,except empty ones

bool("abc")
bool(123)
bool(["jabuka", "trešnja", "banana"])

# False values

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

print(bool(""))

# Functions with a Boolean = isinstance() if object is of a certain data type

x = 200
print(isinstance(x, int))


