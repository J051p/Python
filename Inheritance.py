#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class -> class being inherited from, also called base class.
#Child class -> class inherits from another class, also called derived class.

#Create a Parent class

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    
    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Josip", "Cosic")
x.printname()


#Create a Child class

class Student(Person):
    pass

x = Student("Mike", "Olson")
x.printname() 

#Add the __init__() Function

class Student(Person):
    def __init__(self, fname, lname):
    #add properties etc.
        Person.__init__(self, fname, lname)

x = Student("Mike", "Olson")
x.printname()

#super() function

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = Student("Mike", "Olson")
x.printname()


#Add properties

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduatonyear = 2019

x = Student ("Mike", "Olson")
print(x.graduatonyear)





