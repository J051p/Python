# Two loops -> while and for
# While -> execute a set of statements as long as a condition is true

# print i as long as i is less than 6
i = 1
while i < 6:
    print(i)
    i +=1

# break statement stops the loop even if the while condition is true
# exit the loop when i is 8:

i = 8
while i < 20: # i is less than 20
    print(i)
    if i == 8: # if i is equal to 8
        break # stop the loop
    i +=1


# continue statement stops the current iteration, and continue with the next

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# else statement can run a block of code once when the condition is no longer true

i = 1
while i < 6:
    print(i)
    i += 1
else:
        print ("i is no longer less than 6")