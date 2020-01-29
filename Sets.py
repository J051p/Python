# Collection which is unordered and unindexed. Written in curly brackets {}.

# Create a set
set1 = {"bmw","audi", "mercedes-benz"} # create set
print(set1) # print set

# You cannot access items in a set by refering to an index (unordered)
# We can loop through the set items using a for loop, or use in (specific value)

# Access items
set1 = {"bmw","audi", "mercedes-benz"}

for x in set1:
    print(x)

# Check if bmw is in set1 (if yes -> print True)

set1 = {"bmw","audi", "mercedes-benz"}
print ("bmw" in set1)

# We cannot change items, but we can add new items, use add().
# To add more than one item, use update().

set1 = {"bmw","audi", "mercedes-benz"} 
set1.add("vw") # using add()
print(set1)

set1 = {"bmw","audi", "mercedes-benz"}
set1.update(["ford","volvo","peugeot"]) # using update()
print(set1)

# Lenght of a set
set1 = {"bmw","audi", "mercedes-benz"}
print(len(set1))

# To remove item, use remove() or discard()
set1 = {"bmw","audi", "mercedes-benz"}
set1.remove("audi") # remove()
print(set1)

set1 = {"bmw","audi", "mercedes-benz"}
set1.discard("mercedes-benz") # discard()
print(set1)

# Using pop() we can remove item, but it will remove the last item, since sets are unordered, we cannot know what item got removed

set1 = {"bmw","audi", "mercedes-benz"}
x = set1.pop()
print(x)

# clear() method empties the set

set1 = {"bmw","audi", "mercedes-benz"}
set1.clear()
print(set1)

# del method, delete the set completely

set1 = {"bmw","audi", "mercedes-benz"}
del set1
print(set1)

