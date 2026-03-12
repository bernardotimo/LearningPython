# Arbitrary positional arguments

def sum_all(*args): # args becomes a tuple
    total = 0
    for item in args:
        total += item
    return total
print("Sum:", sum_all(1,2,3,4,5,6))