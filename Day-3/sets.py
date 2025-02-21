#----------------------------SETS:
'''
set is a built-in data type that is used to store unordered collections of 
unique elements. Sets are similar to lists or dictionaries, but they do not 
allow duplicates and they are unordered, meaning the elements have no specific 
order
'''


#---set
data = {1, 2, 3, 4, 5, 6}
print(data)

#---empty set
empty_set = {}
print(empty_set)

#---set-list
list_numbers = [34, 56, 68, 29, 98]
data = set(list_numbers)
print(data)

#---add, remove and discard
numbers = {11, 12, 13, 14, 15}
print(numbers)
#add item but in start
numbers.add(16)
print(numbers)
#removes an item
numbers.remove(12)
print(numbers)
#discard any item like remove
numbers.discard(11)
print(numbers)
#doesn't give any error even if the item is not in the set 
numbers.discard(17)
print(numbers)


#---set operators
set_1 = {1, 2, 3}
set_2 = {3, 4, 5, 6}
#union
union = set_1 | set_2
print(union)
print(set_1.union(set_2))
#intersection
intersection = set_1 & set_2
print(intersection)
print(set_1.intersection(set_2))
#difference
difference = set_1 - set_2
print(difference)
print(set_1.difference(set_2))
#symmetric difference
symmetric_difference = set_1 ^ set_2
print(symmetric_difference)
print(set_1.symmetric_difference(set_2))
#subset
print(set_1.issubset(set_2))
print(set_1 <= set_2)
#superset
print(set_2.issuperset(set_1))
print(set_1 >= set_2)
#disjoint
print(set_1.isdisjoint(set_2))
#frozen
frozen_set = frozenset(set_1)
print(frozen_set)