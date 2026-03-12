print("\n=== MULTIPLE EXCEPTIONS ===")

try:
    value = int("abc")
    result = 10 / value
except ValueError:
    print("The string could not be converted to an integer.")
except ZeroDivisionError:
    print("The string could not be divided by zero.")


print("\n=== CATCHING MULTIPLE EXCEPTIONS ===")

try:
    user_input = "0"
    number = int(user_input)
    result = 100 / number
except (ValueError, ZeroDivisionError) as e:
    print("Exception:", e)