# add(elem) – Adds an element to the set.
my_set = {'mango', 'banana', 'cherry'}
# my_set.add('orange')
# print(my_set)


# clear() – Removes all elements from the set.
# my_set.clear()
# print(my_set)


# copy() – Returns a shallow copy of the set.
# my_set_copy = my_set.copy()
# print(my_set_copy)

# difference(*others) – Returns a set with elements in the set but not in the others.

# my_set2 = {'banana', 'kiwi', 'grape'}
# result = my_set.difference(my_set2)
# print(result)  # Output: {'mango', 'cherry'}

# difference_update(*others) – Removes elements found in others from the set.
# my_set2 = {'banana', 'kiwi', 'grape'}
# my_set.difference_update(my_set2)
# print(my_set)  # Output: {'mango', 'cherry'}

# discard(elem) – Removes an element if present (no error if absent).

# my_set.discard('banana')
# print(my_set)  # Output: {'mango', 'cherry'}

# intersection(*others) – Returns elements common to the set and all others.

my_set2 = {'banana', 'kiwi', 'grape', 'cherry'}
result = my_set.intersection(my_set2)
print(result)  # Output: {'cherry'}

# intersection_update(*others) – Updates the set with only common elements.

my_set2 = {'banana', 'kiwi', 'grape', 'cherry'}
my_set.intersection_update(my_set2)
print(my_set)  # Output: {'cherry'}

# isdisjoint(other) – Returns True if two sets have no elements in common.

my_set2 = {'banana', 'kiwi', 'grape'}
result = my_set.isdisjoint(my_set2) 
print(result)  # Output: True

# issubset(other) – Returns True if the set is a subset of another.
my_set = {'cherry'}
my_set2 = {'banana', 'kiwi', 'grape', 'cherry'} 
result = my_set.issubset(my_set2)
print(result)  # Output: True

# issuperset(other) – Returns True if the set is a superset of another.

my_set = {'banana', 'kiwi', 'grape', 'cherry'}
my_set2 = {'cherry'}
result = my_set.issuperset(my_set2)
print(result)  # Output: True

# pop() – Removes and returns an arbitrary element (error if empty).

my_set = {'mango', 'banana', 'cherry'}
popped_element = my_set.pop()
print(popped_element)  # Output: Arbitrary element, e.g., 'banana'

# remove(elem) – Removes an element (error if absent).
my_set = {'mango', 'banana', 'cherry'}
my_set.remove('banana') 
print(my_set)  # Output: {'mango', 'cherry'}

# symmetric_difference(other) – Returns elements in either set, but not both.
my_set = {'mango', 'banana', 'cherry'}
my_set2 = {'banana', 'kiwi', 'grape'}   
result = my_set.symmetric_difference(my_set2)
print(result)  # Output: {'mango', 'cherry', 'kiwi'


# symmetric_difference_update(other) – Updates the set with symmetric difference.
my_set = {'mango', 'banana', 'cherry'}
my_set2 = {'banana', 'kiwi', 'grape'}
my_set.symmetric_difference_update(my_set2)
print(my_set)  # Output: {'mango', 'cherry', 'kiwi


# union(*others) – Returns a set with all elements from the set and others. 
my_set = {'mango', 'banana', 'cherry'}
my_set2 = {'banana', 'kiwi', 'grape'}   
result = my_set.union(my_set2)
print(result)  # Output: {'mango', 'cherry', 'kiwi',


# update(*others) – Adds elements from others to the set.
my_set = {'mango', 'banana', 'cherry'}
my_set2 = {'banana', 'kiwi', 'grape'}   
my_set.update(my_set2)
print(my_set)  # Output: {'mango', 'cherry', 'kiwi
