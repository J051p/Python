# A block of code which only runs when it is called, you can pass data (parameters), returns data as a result.

# Creating function

def moja_funkcija(): # definiranje
    print("Pozdrav iz funkcije")

# Calling  a function

def moja_funkcija():
    print("Pozdrav iz funkcije")
moja_funkcija() # pozivanje funkcije,daje print

# Broj funkcija - test

def broj_funkcija(): # definiranje
    a = 5 # definiranje varijabli
    b = 5
    c = a + b
    print(c) # zbroj varijabli je 10
broj_funkcija() # vraća broj 10

# Arguments -> information can be passed into functions as arguments
# Specified after the function name, inside parentheses, separated with comma

def moja_funkcija(fname):
    print(fname + " Refsnes")

moja_funkcija("Josip")
moja_funkcija("Emma")

# Number of arguments

def moja_funkcija(fname, lname, age): # arguments are ime, prezime i dob
    print(fname + " " + lname, age) # printing args

moja_funkcija("Josip", "Ćosić", 24) # result

# Arbitary arguments, *args
# Unknown number of args, just add * before the parameter

def moja_funkcija(*cars):
    print("The best car is " + cars[2])

moja_funkcija("Bmw", "Audi", "VW")

# Keyword args (kwargs), key = value syntax

def moja_funkcija(car1, car2, car3):
    print("The best car is " + car1)

moja_funkcija(car1 = "Bmw", car2 = "Audi", car3 = "VW")

# Kwargs, add ** before the parameter name in the function definition

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "George", lname = "Boi")

# Default parametar value

def my_function(country = "Croatia"):
    print("I am from " + country)

my_function("Sweden")
my_function()

# Passing a list as an argument

def my_function(fruits):
    for x in fruits:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return value

def my_function(x):
    return 6 * x

print(my_function(2))
print(my_function(3))
print(my_function(4))

