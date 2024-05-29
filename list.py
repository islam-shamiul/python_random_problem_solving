age=[20,50,40,10,5,100,15]

print(age[:5]) #slicing

# The append() method adds an item at the end of the list
age.append(30)
age.append(20)
print(age)

# We use the extend() method to add all the items of an iterable to the end of the list
age2=[20,22,33,44,18]
age.extend(age2)
print(age)

# We use the insert() method to add an element at the specified index
age.insert(2,60)
print(age)

# Python lists are mutable. Meaning lists are changeable
age[4]=5
age[5]=10
print(age)

# removes item present at the given index
age.remove(5)
print(age)

# we can use the del statement to remove one or more items from a list
del age[8]
print(age)    

# get the index of specific elements
index = age.index(100)
print(index)

# The count() method returns the number of times the specified element appears in the list.
count = age.count(20)
print(count)

# The list pop() method removes the item at the specified index. The method also returns the removed item
removed_element = age.pop(8)
print('Removed Element:', removed_element)
print('Updated List:', age)

# age.pop()
# print(age)

# The reverse() method reverses the elements of the list.

