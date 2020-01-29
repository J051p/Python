# Everything is an object, with its propeties and methods

# Create a class

class Mojaklasa:
    x = 10
print(Mojaklasa)

# Create object

p1 = Mojaklasa()
print(p1.x)

# _init_() function -> use to assign values to object properties, always executed when the class is being created.

class Auto:
    def __init__(self, name, model, year):
        self.name = name        # self se može zamijeniti s bilo kojim nazivom, ali mora biti prvi parametar u klasi
        self.model = model      # stvaranje klase s atributima
        self.year = year
    
    def mojafunkcija(self): # stvaranje funkcije za ispis
        print("Pozdrav, današnji auto je " + self.name)

p1 = Auto("Bmw","E46", 2004)

print(p1.name)
print(p1.model)       # printanje atributa
print(p1.year)

p1.mojafunkcija()     # printanje funkcije za ispis

