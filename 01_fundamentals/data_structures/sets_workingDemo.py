# Sets - contain unique information - don't have index
a = {1, 2, 3, 3, 3} # No : means is a set
b = {3, 4, 5}
print("a:", a) #duplicates removed
print("b:", b)

# Add / remove - values cannot be changed
a.add(10)
print("Add a:", a)

a.discard(2) # no error if missing
print("Discard a:", a)

# Membership (fast)
print("10 in a:", 10 in a)

# Set operations
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric diff:", a ^ b)

# Practical use - ideal to identify and remove duplicates
items = ["bread", "bread", "donut", "donut", "muffin"]
unique_items = set(items)
print("Unique items:", unique_items)

# Sort
print(sorted(unique_items)) 