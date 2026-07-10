# input() - reads what the user types from the keyboard
# IMPORTANT: input() ALWAYS returns a string

name = input("What is your name? ")
print("Hello,", name)
print(type(name))  # <class 'str'>

# Type conversion - the text is a string, convert it to do math
age = input("How old are you? ")
age = int(age)              # str -> int
print("Next year you will be", age + 1)

# You can convert directly on the same line
height = float(input("Your height in meters? "))
print(type(height))        # <class 'float'>

# Combining with f-strings (already learned in strings/)
city = input("Which city do you live in? ")
print(f"{name} is {age} years old and lives in {city}")

# Combining with conditionals (already learned in control_flow/)
number = int(input("Type a number: "))
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")