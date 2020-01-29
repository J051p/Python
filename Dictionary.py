# Collection which is unoredered and indexed. Written with curly brackets, and they have keys and values.

# Create and print dictionary

dict = {
    "brand": "Bmw",
    "model": "Series 3",
    "year": 2001
}
print (dict)

# Accessing items

dict = {
    "brand": "Bmw",
    "model": "Series 3",
    "year": 2001
}
x = dict ["brand"] # get item 
print(x)

# Using get()

dict = {
    "brand": "Bmw",
    "model": "Series 3",
    "year": 2001
}
x = dict.get("year")
print(x)

# Change values

dict = {
    "brand": "Bmw",
    "model": "Series 3",
    "year": 2001
}
dict["year"] = 2019
print(dict)

# Loop through a dictionary, print all key names

dict = {
    "brand": "Bmw",
    "model": "Series 3",
    "year": 2001
}
for x in dict: # using for
    print(x)

# Print all values in the dictionary

dict = {
    "brand": "Bmw",
    "model": "Series 3",
    "year": 2001
}
for x in dict:
    print(dict[x])

# Use values() function to return values of a dictionary

dict = {
    "brand": "Bmw",
    "model": "Series 3",
    "year": 2001
}
for x in dict.values():
    print(x)

# Loop through keys and values,using items()
dict = {
    "brand": "Bmw",
    "model": "Series 3",
    "year": 2001
}
for x,y in dict.items():
    print(x, y)

# Check if key exists using in 

dict = {
    "brand": "Bmw",
    "model": "Series 3",
    "year": 2001
}

if "model" in dict:
    print ("Yes, model is present in this dict dictionary")

# Dictionary lenght

dict = {
    "brand": "Bmw",
    "model": "Series 3",
    "year": 2001
}
print(len(dict))

# Adding items

dict = {
    "brand": "Bmw",
    "model": "Series 3",
    "year": 2001
}
dict["color"] = "black"
print(dict)

# Removing items

dict = {
    "brand": "Bmw",
    "model": "Series 3",
    "year": 2001
}
dict.pop("year")
print(dict)

# Deleting items (clear() empties the dictionary)

dict = {
    "brand": "Bmw",
    "model": "Series 3",
    "year": 2001
}
del dict["year"]
print(dict)

# Making a copy of a dictionary

dict = {
    "brand": "Bmw",
    "model": "Series 3",
    "year": 2001
}
mydict = dict.copy()
print(mydict)

# Nested dictionary

car1 = {
    "brand" : "Bmw",
    "model" : "Series 3",
    "year" : 2019
}

car2 = {
    "brand" : "Bmw",
    "model" : "X5",
    "year": 2019
}

mycars = {
    "car1" : car1,
    "car2" : car2,
}

print(mycars)
