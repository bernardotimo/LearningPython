# Formatting: building strings from values
# This file covers .format() and f-strings.
# For the classic % operator see formatOperatorDemo.py
# Full explanation in FORMATTING.md

name = "Bernardo"
age = 22

# f-string (modern, recommended) vs .format() method
print(f"My name is {name} and I am {age} years old")
print("My name is {} and I am {} years old".format(name, age))

# .format() by position index and by name
print("{0} {1} {0}".format("a", "b"))          # reuse values -> a b a
print("{n} is {a}".format(n="Ana", a=30))      # named placeholders

# Expressions inside f-strings
a = 10
b = 5
print(f"The sum is {a + b}")

# Method calls inside f-strings
word = "python"
print(f"Uppercase: {word.upper()}")

# Self-documenting expressions with = (great for debugging)
print(f"{a + b = }")                           # a + b = 15

# Decimal places
pi = 3.14159265
print(f"{pi:.2f}")

# Thousands separator
number = 1000000
print(f"{number:,}")

# Percentage
score = 0.87
print(f"{score:.2%}")

# Alignment: < left, > right, ^ center (width = 10, filled with dashes)
label = "hi"
print(f"|{label:<10}|")
print(f"|{label:>10}|")
print(f"|{label:^10}|")
print(f"|{label:-^10}|")                       # custom fill char

# Table: left-aligned name, right-aligned price with 2 decimals
products = [
    ("Apple", 1.20),
    ("Banana", 0.50),
    ("Orange", 0.80)
]

for product, price in products:
    print(f"{product:<10} ${price:>5.2f}")
