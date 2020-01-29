# Collection which is ordered and changeable, written in square brackets.

# Create a list:

lista = ["Josip", "Emma", "Bella", "Pip"]
print(lista)

# Access items in a list:

lista = ["Josip", "Emma", "Bella", "Pip"]
print(lista[1])

# Negative indexing = beginning from the end, -1 (last item), -2 (second last)

lista = ["Josip", "Emma", "Bella", "Pip"]
print(lista[-1])

# Range of indexes, where to start and where to end

lista = ["Josip", "Emma", "Bella", "Pip"]
print(lista[0:3])

# Range of negative indexes, where to start and where to end

lista = ["Josip", "Emma", "Bella", "Pip"]
print(lista[-0:-3])

# Change item value (from Pip to Simon)

lista = ["Josip", "Emma", "Bella", "Pip"]
lista[3] = "Simon"
print(lista)

# Loop through a list, one by one

lista = ["Josip", "Emma", "Bella", "Pip"]
for x in lista:
    print(x)

# Check if item exists

lista = ["Josip", "Emma", "Bella", "Pip"]
if "Josip" in lista:
    print ("He's here")

# List lenght

lista = ["Josip", "Emma", "Bella", "Pip"]
print(len(lista))

# Add items (append = 1 item), insert()=specified index

lista = ["Josip", "Emma", "Bella", "Pip"]
lista.append("Marina")
print(lista)

# Insert()

lista = ["Josip", "Emma", "Bella", "Pip"]
lista.insert(1,"Marina")
print(lista)

# Remove item = remove, pop()=removes specified index, del -> name of a list=deletes list completely
# clear -> name of a list = empties the list
lista = ["Josip", "Emma", "Bella", "Pip"]
lista.remove("Josip")
print(lista)

# Create a copy of a list (.copy)/list

lista = ["Josip", "Emma", "Bella", "Pip"]
mojalista = lista.copy()
print(mojalista)

# Join two lists

lista1 = ["a","b","c"]
lista2 = ["1","2","3"]

lista3 = lista1 + lista2
print(lista3)





