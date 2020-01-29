# Spajanje stringova (dodavanje spacea između = " ")

a = "Danas je "
b = "nedjelja"
c = ",27.listopada 2019.godine "
d = a + b + c

print(d)

# String format = format() = numbers into strings, use {0} to place arguments in order

age = 24
txt = "My name is Josip, and I am {}"
print(txt.format(age))

vehicle = "Bmw e46 320d"
age = 2004
horsepower = 150
price = 3000

txt = "I would like to buy {} from {} with {} horsepower for around {} euros."
print(txt.format(vehicle, age, horsepower, price))

