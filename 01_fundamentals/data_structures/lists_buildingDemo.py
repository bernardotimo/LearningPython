# Lists - multiples variables in a single variable
numbers = [1, 2, 3, 4, 5, 6]
print(numbers)

# Data type
print(type(numbers))

# Append - add one item
numbers.append(7)
print("Append:", numbers)

# Extend - add many items
numbers.extend([8, 9])
print("Extend:", numbers)

# Insert - add at index
numbers.insert(0, 0)
print("Insert:", numbers)

# Remove by value - first match
numbers.remove(3)
print("Remove:", numbers)

# Pop - remove by index, default last
last = numbers.pop()
print("Pop:", last, "| list:", numbers)

# Sort (in-place) vs sorted (new list)
numbers.sort()
print("Sort:", numbers)
print("sorted(desc):", sorted(numbers, reverse=True))

# List comprehension (fast, clean build)
squares = [n * n for n in numbers]
print("Squares:", squares)