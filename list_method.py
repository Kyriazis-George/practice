# Start with a base list
names = ["Alice", "Bob", "Charlie"]

# -------------------------------
# LIST METHODS
# -------------------------------

# 1. append() -> add item to the end
names.append("Diana")
print("append:", names)

# 2. clear() -> remove all items
copy_for_clear = names.copy()
copy_for_clear.clear()
print("clear:", copy_for_clear)

# 3. copy() -> return a shallow copy
names_copy = names.copy()
print("copy:", names_copy)

# 4. count() -> count occurrences of an item
names.append("Alice")
print("count:", names.count("Alice"))

# 5. extend() -> add multiple items
names.extend(["Ethan", "Fiona"])
print("extend:", names)

# 6. index() -> get position of first occurrence
print("index of 'Charlie':", names.index("Charlie"))

# 7. insert() -> add at specific position
names.insert(1, "George")
print("insert:", names)

# 8. pop() -> remove and return item (last by default)
popped = names.pop()
print("pop:", names, "| removed:", popped)

# 9. remove() -> remove first occurrence
names.remove("Alice")
print("remove:", names)

# 10. reverse() -> reverse the list in place
names.reverse()
print("reverse:", names)

# 11. sort() -> sort alphabetically
names.sort()
print("sort:", names)


# -------------------------------
# LIST COMPREHENSIONS
# -------------------------------

# Original list again for comprehension examples
names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

# 1. Simple copy
copy_comp = [name for name in names]
print("comprehension copy:", copy_comp)

# 2. Filtering -> names that start with 'C'
starts_with_c = [name for name in names if name.startswith("C")]
print("filter comprehension:", starts_with_c)

# 3. Mapping -> all names uppercased
uppercased = [name.upper() for name in names]
print("map comprehension:", uppercased)

# 4. Conditional mapping -> uppercase if starts with 'A', else lowercase
conditional_map = [name.upper() if name.startswith("A") else name.lower() for name in names]
print("conditional map comprehension:", conditional_map)

# 5. Nested loop -> flatten a 2D list
nested = [["Alice", "Bob"], ["Charlie", "Diana"], ["Ethan"]]
flattened = [name for sublist in nested for name in sublist]
print("flatten comprehension:", flattened)

# 6. Transform with function -> length of each name
lengths = [len(name) for name in names]
print("lengths comprehension:", lengths)
