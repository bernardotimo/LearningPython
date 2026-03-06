# Conditionals Operators
age = 17
has_id = True

if age >= 18 and has_id:
    print("Access granted")
elif age >= 18 and not has_id:
    print("Access denied: missing ID")
else:
    print("Access denied: underage")

score = 82
result = "pass" if score >= 70 else "fail"
print("Ternary result:", result)

# Comparison chain
x = 7
print("5 < x < 10", 5 < x < 10)

# Truthy / falsy
items = []
if items:
    print("List has items")
else:
    print("Empty list is falsy") # It is not boolean false, that is why it is falsy

name = "Bernardo"
if name and len(name) > 3:
    print("Valid name")