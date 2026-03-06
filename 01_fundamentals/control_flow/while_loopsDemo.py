# Repeats a block as long as a condition remains true

ingredients_to_add = 5
items_added = 0
while ingredients_to_add > 0:
    ingredients_to_add -= 1
    items_added += 1
    if items_added == 1:
        print(items_added, "item added")
    else:
        print(items_added, "items added")

# Infinit loop - used in servers, game loops, event listeners
while True:
    command = input("Type 'quit' to exit: ")

    if command == "quit":
        break

# Input validation
password = ""

while password != "python123":
    password = input("Enter password: ")
print("Access granted")

# Accumulator
total = 0
number = 1
while number <= 5:
    total += number
    number += 1
print(total)

# Counting down
count = 5
while count > 0:
    print(count)
    count -= 1
print("Lift off!")

# Loop with lists - for loops are preferred for lists
animals = ["chicken", "pig", "cow"]
index = 0
while index < len(animals):
    print(animals[index])
    index += 1

# Processing and removing items
tasks = ["task1", "task2", "task3"]
while tasks:
    current_task = tasks.pop()
    print("Processing:", current_task)

# Sentinel controlled
num = None

while num != 0:
    num = int(input("Enter a number: "))

# Nested while loop
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(i, j)
        j += 1
    i += 1

# While with else - if break happens, else will not execute
number = 1
while number <= 3:
    print(number)
    number += 1
else:
    print("Loop finished")