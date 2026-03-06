# For each value in the sequence, perform this action
# Sequence = iterable e.g., list, dictionary, etc
# Value = iterator e.g., the index - can give it any name
from statistics import quantiles

# Example 1
quantities = [1000, 500, 650, 50, 788, 26]
for q in quantities:
    if q > 500:
        print("Plenty in stock")
    elif q >= 100:
        print("Enough")
    else:
        print("Nearly out")

# Loop through strings
ingredient_name = "Pasta"
for i in ingredient_name:
    print(i)

# Accumulator
numbers = [10, 20, 30, 40, 50]
total = 0
for n in numbers:
    total += n
print(total)

# Loop through dictionaries
# Key only or value only
fruits = {"apple": 10, "banana": 20, "cherry": 30}
for fruit in fruits.keys():
    print("Keys:", fruit)
for fruit in fruits.values():
    print("Values:", fruit)

# Key and Value
number_of_students = {"Ana": 2, "Brannon": 1, "John": 5}
for student, num in number_of_students.items():
    print(student, ":", num)

# Index + value - enumerate()
cars = ["ford", "bmw", "toyota"]
for index, car in enumerate(cars):
    print(index, car)

# Range
for i in range(1, 6):
    print(i)

# Looping through two lists (zip)
names = ["John", "Bernardo", "Aurora", "Alicia"]
scores = [90, 80, 70, 60]
for name, score in zip(names, scores):
    print(name, score)

# Nested for loop
for i in range(5):
    for j in range(3):
        print(i, j)

# Break statement - stops the loop immediately
num = [10, 20, 30, 40, 50]
for n in num:
    if n == 30:
        break
    print(n)

# Continue statement - skips the current iteration
num1 = [10, 20, 30, 40, 50]
for n in num1:
    if n == 30:
        continue
    print(n)

# List building with append
grades = [90, 80, 70, 60]
extra_grades = []
for g in grades:
    if g > 60:
        extra_grades.append(g * 1.1)
for grade in extra_grades:
    print(f"Grades with bonus: {grade:.2f}")