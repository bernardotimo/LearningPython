print("\n=== CUSTOM EXCEPTIONS ===")

class NegativeNumberError(Exception):
    """Raised when negative number is not allowed"""
    pass
def square_root(num):
    if num < 0:
        raise NegativeNumberError("Negatives are not allowed")
    return num ** 2

try:
    print(square_root(-1))
except NegativeNumberError as e:
    print("NegativeNumberError:", e)
