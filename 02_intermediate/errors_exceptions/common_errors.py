# Syntax errors happens before the program runs, so cannot be caught with try/except
print("\n=== TYPE ERROR ===")

# Incompatible data type
try:
    result = "5" + 3
except TypeError as e:
    print("TypeError:", e)


print("\n=== VALUE ERROR ===")

# Value not within an acceptable range
try:
    number = int("Hello")
except ValueError as e:
    print("ValueError:", e)


print("\n=== ZERO DIVISION ERROR ===")

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)


print("\n=== INDEX ERROR ===")

try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError as e:
    print("IndexError:", e)


print("\n=== KEY ERROR ===")

try:
    person = {"name": "John", "age": 25}
    print(person["city"])
except KeyError as e:
    print("KeyError:", e)


print("\n=== FILE NOT FOUND ERROR ===")

try:
    with open("file.txt", "r") as f:
        contents = f.read()
except FileNotFoundError as e:
    print("FileNotFoundError:", e)


