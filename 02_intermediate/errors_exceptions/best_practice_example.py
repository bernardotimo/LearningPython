print("\n=== CUSTOM EXCEPTIONS ===")

def safe_divide(a, b):
    """
    Divide two numbers safely

    Returns:
         float or None
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
print("Safe division (10, 2): ", safe_divide(10, 2))
print("Safe division (10, 0): ", safe_divide(10, 0))