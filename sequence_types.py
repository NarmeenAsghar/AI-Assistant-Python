#------------------------------SEQUENCE TYPES:
'''
Sequence types are data types that allow you to store multiple items in an ordered manner. 
The elements in a sequence are indexed, and each element has a position (index) associated with it
'''

#---Stirng:
'''
A string is a series of characters.Anything inside quotes are considered as a string
'''

variable = "Starting new journey in the world of AI Python"
print(variable)

name = "david John"
print(name.upper())
print(name.lower())
print(name.title())


#---f string:
'''
f in string are for format,  because python formats the string by replacing the name of any variable in braces with its value
'''

first_name = "Daisy"
last_name = "Warner"
full_name = f"{first_name} {last_name}"
print(f"Hello {full_name}, How are you?")


#---Boolean:
'''
Represents a Boolean value (True or False)
'''

is_active = True
is_sunny = False
print(is_active) 
print(is_sunny) 


#---List:
'''
List is a collection of items in a particular order.
'''

items = ['apple', 'juice', 45, 87, ['fans', 'bulbs'], [2, 3]]
print(items)
print(items[2])
print(items[-1])
#adding elements in list using append
items.append(32.4)
print(items)
#inserting items in list on specific position by indexing
items.insert(0, 'mangoes')
print(items)
#removing items in list using pop
items.pop()
print(items)
#items deleting by del
del items[3]
print(items)
#removing items by using remove
items.remove([2, 3])
print(items)


''' Sorting data from list '''

data = [54.2, 85, 65, 75, 22.7]
#sorting list items
data.sort()
print(data)
#sorting items by reverse method
data.sort(reverse=True)
print(data)


#---Tuple:
'''
Python refers to values that cannot change as immutable(constant), and an immutable list is called tuple
'''

tuple_data = (10, 20, 30, 'hello', [1, 2])

#tuple through indexing
print(tuple_data[0])
print(tuple_data[3])
print(tuple_data[-1]) 

#slicing a tuple
print(tuple_data[1:4]) 

#Length of a tuple
print(len(tuple_data))

#Checking if an item exists in a tuple
print(20 in tuple_data) 
print('apple' in tuple_data) 

#---Nested tuple:
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple[2]) 


#---Range:
'''
A range in Python is a built-in function that generates an immutable sequence of numbers, 
which is commonly used for iteration in for loops. It allows you to specify a start, stop, 
and step value to generate the desired range of number
'''

#Basic
for i in range(5):
    print(i)

#with start and stop value
for i in range(2, 6):
    print(i)

#with start, stop and step values
for i in range(1, 10, 2):
    print(i)

#reverse itration
for i in range(10, 0, -2):
    print(i)


#---Bytes:
'''
A bytes object is an immutable sequence of bytes. This means that once a bytes object is created, its content cannot be modified
'''

b = b'hello'  # Using the 'b' for representing bytes
print(b)

#indexing of byte
print(b[0])  #Output: 104 (ASCII value of 'h')

#slicing bytes value
print(b[1:4])

#trying to modify
# b[0] = 72   generate an error


#---Bytearray:
'''
 A bytearray is a mutable sequence of bytes. Unlike bytes, you can modify the content of a 
 bytearray object (you can change, append, or remove bytes)
'''

ba = bytearray(b'hello')
print(ba)

#Modifying (mutable)
ba[0] = 72  # Change 'h' to 'H' (ASCII value of 'H' is 72)
print(ba)

#Appending
ba.append(33)
print(ba)

#Removing a byte
ba.remove(101)
print(ba)


#---Set:
'''
set is an unordered collection of unique items. Sets are useful when you need to store multiple items, 
but you don't care about the order of the items and want to avoid duplicates
'''

fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)

#Adding
fruits.add("orange")
print(fruits)

#Removing
fruits.remove("banana")
print(fruits)

#Removing an element using discard()
fruits.discard("pear")
print(fruits)

#Clearing the set
fruits.clear()
print(fruits)

#Adding elements again
fruits = {"apple", "banana", "cherry"}

#Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set) 

#Intersection
intersection_set = set1 & set2
print(intersection_set)

#Difference
difference_set = set1 - set2
print(difference_set)
