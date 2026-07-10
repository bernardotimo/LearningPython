# The % operator - the classic "string formatting operator"
# Syntax: "template with %placeholders" % (values)

# %s - string, %d - integer, %f - float
name = "Bernardo"
age = 22
print("My name is %s and I am %d years old" % (name, age))

# A single value does not need parentheses
print("Hello, %s" % name)

# %f defaults to 6 decimal places
pi = 3.14159265
print("Pi is %f" % pi)

# Controlling decimal places: %.2f
print("Pi rounded: %.2f" % pi)

# Width and alignment
# %5d  -> right aligned in 5 spaces
# %-5d -> left aligned in 5 spaces
print("Number:|%5d|" % 42)
print("Number:|%-5d|" % 42)

# Padding floats: width.precision
print("Price:|%8.2f|" % 3.5)

# %x - hexadecimal, %o - octal, %e - scientific
print("Hex: %x" % 255)
print("Scientific: %e" % 1000000)

# A literal percent sign needs %%
print("Discount of %d%%" % 50)

# Named placeholders with a dictionary
person = {"name": "Ana", "age": 30}
print("%(name)s is %(age)d years old" % person)

# Table using the % operator
products = [
    ("Apple", 1.20),
    ("Banana", 0.50),
    ("Orange", 0.80)
]

for product, price in products:
    print("%-10s $%5.2f" % (product, price))
