# Represents an anonymous function
# Does not require a name or need to be saved as a variable
# Structure -> lambda arguments: expression
# Convention is to use x for single argument
# The expression is the equivalent of the function body
# No return statement is required
# Can be stored as a variable

print("\n=== BASIC EXPRESSION  ===")

add = lambda a, b: a + b
print(add(1, 2))


print("\n=== INLINE LAMBDA  ===")

result = (lambda x: x * 2)(10) # 10 defines x
print(result)

average = (lambda x: sum(x)/len(x))([5, 10, 15]) # values defines x
print(average)


print("\n=== STORING AND CALLING  ===")

average_distance = (lambda x: sum(x)/len(x))
print(average_distance([30, 60, 90]))


print("\n=== LAMBDA WITH MAP()  ===") # applies a function to all elements in an iterable

numbers = [1, 2, 3, 4, 5]
double = list(map(lambda x: x * 2, numbers)) # convert to a list (data structure)
print("Original list:", numbers)
print("Double list:", double)

colleagues = ["Sarah Martinez", "Michael Chen", "Emily Brown"]
cleaned = map(lambda x: x.replace(" ", "_").lower(), colleagues)
cleaned_list = list(cleaned)
print(cleaned_list)


print("\n=== LAMBDA WITH FILTER()  ===")

numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers)) # filter keeps elements that returns true
print("Even numbers:", evens)


print("\n=== LAMBDA WITH SORTED()  ===")

students = [
    ("Alice", 90),
    ("John", 80),
    ("Charlie", 70),
]

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)


print("\n=== MULTIPLE ARGUMENTS  ===")

multiple_arguments = lambda a, b, c: a * b + c
print(multiple_arguments(1, 2, 10))


print("\n=== LAMBDA WITH CONDITIONAL  ===")

check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(2))
print(check_even(3))


print("\n=== LAMBDA RETURNING FUNCTION  ===")

def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(10))
print(triple(10))


print("\n=== SORTING DICTIONARIES  ===")

products = [
    {"name": "Laptop", "price": 100},
    {"name": "Mouse", "price": 200},
    {"name": "Keyboard", "price": 300}
]

sorted_products = sorted(products, key=lambda x: x["price"])
print(sorted_products)


print("\n=== LIST COMPREHENSION  ===")

square = lambda x: x**2
squares = [square(x) for x in range(6)]
print(squares)