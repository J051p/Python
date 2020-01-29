# Used to store multiple values in one single variable.

# Create an array

cars = ["Bmw", "Volvo","Audi"]
print(cars)

# Access array

cars = ["Bmw", "Volvo","Audi"]
x = cars[1]
print(x)

# Modify

cars = ["Bmw", "Volvo","Audi"]
cars[1] = "Mercedes"
print(cars)

# Lenght

cars = ["Bmw", "Volvo","Audi"]
x = len(cars)
print(x)

# Looping

cars = ["Bmw", "Volvo","Audi"]
for x in cars:
    print(x)

# Adding array elements

cars = ["Bmw", "Volvo","Audi"]
cars.append("Honda")
print(cars)

# Remove array element

cars = ["Bmw", "Volvo","Audi"]
cars.pop(1) # cars.remove("Volvo")
print(cars)

