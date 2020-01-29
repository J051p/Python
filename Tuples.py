# Collection which is ordered and unchangeable with round brackets ().

# Create a tuple

thistuple = ("apple","banana", "cherry")
print(thistuple)

# Access tuple items -> [2]=cherry 

thistuple = ("apple","banana", "cherry")
print(thistuple[2])

# Negative indexing

thistuple = ("apple","banana", "cherry")
print(thistuple[-2])

# Range of indexes

thistuple = ("apple","banana", "cherry","pear","watermelon")
print(thistuple[0:3])

# Range of negative indexes

thistuple = ("apple","banana", "cherry","pear","watermelon")
print(thistuple[-0:-3])

# Change tuple values = convert tuple into a list, change the list and convert back to tuple

x = ("mango","apple")
y = list(x) # tuple into a list

y[1]= "kiwi" # change apple to kiwi
x = tuple(y) # convert back to tuple

print(x)

# Loop through a tuple
thistuple = ("apple","banana", "cherry","pear","watermelon")
for x in thistuple:
    print(x)

# Check if item exists

thistuple = ("apple","banana", "cherry","pear","watermelon")
if "apple" in thistuple:
    print ("Apple is in there")

# Tuple lenght

thistuple = ("apple","banana", "cherry","pear","watermelon")
print(len(thistuple))

# Tuple with one item (add coma (,))

thattuple = ("jabolko",)
print(type(thattuple))

# delete tuple -> del thattuple, thistuple

# Join two tuples

tuple1 = ("apple","mango")
tuple2 = ("pear", "fruit")
tuple3 = tuple1 + tuple2
print(tuple3)

# Tuple methods -> count()/index()