# Raise will produce an error, avoiding executing subsequent one
print("\n=== RAISING EXCEPTIONS ===")

def divide(a, b):
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b
try:
    print(divide(1, 0))
except ValueError as e:
    print("ValueError:", e)