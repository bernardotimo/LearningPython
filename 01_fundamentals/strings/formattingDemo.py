# Formatting
name = "Bernardo"
age = 22
print(f"My name is {name} and I am {age} years old")
print("My name is {} and I am {} years old".format(name, age))

# Operations
a = 10
b = 5

print(f"The sum is {a + b}")

# Methods
name = "python"
print(f"Uppercase: {name.upper()}")

# Decimal
pi = 3.14159265
print(f"{pi:.2f}")

# Separators
number = 1000000
print(f"{number:,}")

# Percentage
score = 0.87
print(f"{score:.2%}")

# Tables
products = [
    ("Apple", 1.20),
    ("Banana", 0.50),
    ("Orange", 0.80)
]

for name, price in products:
    print(f"{name:<10} ${price:>5.2f}")