x = 1 #float
y = 2.8 #float
z = 1j #complex

#from int to float
a = float(x)

#from float to int
b = int(y)

#from int to complex
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#random number

import random

print (random.randrange(1,15))