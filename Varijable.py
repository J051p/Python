x = 5 #deklariranje varijabli
y = "John"

print (x) #ispis varijabli
print (y)

a, b, c = "A", "B", "C"
print (a)
print (b)
print (c)

x = "super"
print ("Python je " + x) #kombinacija s + (spajanje varijabli i teksta)

p = 5 
d = 10
print (p + d)

#Globalne varijable (varijabla izvan funkcije)

x = "super"

def myfunc():
    print("Python je " + x)

myfunc()

#Globalne varijable (varijabla unutar funkcije)

x = "great"

def myfunc():
    x = "extra"
    print("Python je " + x)

myfunc()

print("Python je " + x)






