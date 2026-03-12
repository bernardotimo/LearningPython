# Help build features with less code

# Mathematical
print("\n=== MATHEMATICAL FUNCTIONS ===")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))
print("Length:", len(numbers))


print("\n=== ROUNDING AND ABSOLUTE ===")

value = -12.7
print("Absolute:", abs(value))
print("Rounded:", round(3.14159, 2))


print("\n=== SORTING ===")

numbers = [10, 20, 30]
letters = ["f", "d", "c"]
print("Sorted:", sorted(numbers))
print("Sorted:", sorted(letters))


print("\n=== ITERATION HELPERS ===")

letters = ["a", "b", "c"]
for i, letter in enumerate(letters):
    print(i, letter)


print("\n=== ZIP FUNCTIONS ===")

names = ["John", "Michael", "David"]
scores = [90, 80, 70]
for name, score in zip(names, scores):
    print(name, score)


print("\n=== RANGE FUNCTIONS ===")

for i in range(5):
    print(i)


print("\n=== ANY AND ALL ===")

conditions = [True, False, False, True]
print("Any true:", any(conditions))
print("All true:", all(conditions))


print("\n=== INPUT FUNCTIONS ===")

name = input("Enter your name: ")
print("Hello", name)


print("\n=== ID FUNCTIONS ===")

a = 10
b = 20
print("ID of a:", id(a))
print("ID of b:", id(b))


print("\n=== MAP FUNCTIONS ===")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)