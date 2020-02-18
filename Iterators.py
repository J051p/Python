#An object that contains a countable number of values.
#Consists of the methods __iter__() and __next__().

#Looping through an iterator

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)


#Create an iterator

class MojiBrojevi:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a +=1
        return x
    
myclass = MojiBrojevi()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))




