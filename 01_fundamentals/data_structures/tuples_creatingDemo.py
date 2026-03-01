# Creating a tuple - cannot be changed
# No adding values
# No removing values
# No changing values
# Can access elements through index
point = (10, 20)
print("Point:", point)

# Tuple unpacking
x, y = point # Useful for location information or identifiers
print("X:", x)
print("Y:", y)

# Single-element tuple needs a comma
single = ("only_one",)
print("single:", single, "| type:", type(single))

# Immutability demo
colors = ("red", "green", "blue")
print("colors:", colors)

# Can't do colors[0] = "pink"