# 'hello' = "hello"
print("Hello")
print('Hello')

# Dodavanje vrijednosti stringu

a = "Hello" 
print(a)

b = """Danas je nedjelja, 27.listopada 2019.godine."""
print(b)

c = '''Danas je nedjelja, 27.listopada 2019.godine.'''
print( c)

# Slicing = slova od pozicije 3 pa do 6

d = "Hello, World!"
print(d[3:6])

# Negative indexing = početak slicanja od kraja stringa

e = "Hello, World!"
print(e[-5:-2])

# Dužina stringa = len()

a = "Josip"
print(len(a))

# Metode stringova = strip miče prazna mjesta 

a = "   Pozdrav svima!   "
print(a.strip())

# Lower() = vraća string malim slovima, Upper() = velika slova vraća, Replace() = mijenja string stringom

b = "Velika slova"
print(b.lower())
print(b.upper())
print(b.replace("V", "O"))

# Split = dijeli stringove u substringove ako nađe instance separatora

a = "Hello, World!"
print(a.split(","))

# Check stringova = ako je pozitivno, ispisuje Boolean (True) ili False

txt = "Danas je nedjelja, sunčan je dan"
x = "elja" in txt
print(x)

txt = "Danas je nedjelja, sunčan je dan"
x = "elja" not in txt
print(x)