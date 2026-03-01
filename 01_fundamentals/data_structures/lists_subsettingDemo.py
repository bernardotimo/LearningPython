# Subsetting lists
letters = ["a", "b", "c", "d", "e", "f"]
print("Letters:", letters)

print("First letter:", letters[0]) # Indexing
print("Last letter:", letters[-1])

print("letters[1:4]:", letters[1:4])   # Slicing
print("letters[:3]:", letters[:3])     # Slicing
print("letters[3:]:", letters[3:])     # Slicing
print("letters[::2]:", letters[::2])   # Stepping - [index::steps]
print("letters[::-1]:", letters[::-1]) # Stepping - reversed list
print("letters[1::2]:", letters[0::3]) # Stepping

# Safe pattern - check length before accessing
if len(letters) > 10:
    print(letters[10])
else:
    print("Index 10 does not exist")