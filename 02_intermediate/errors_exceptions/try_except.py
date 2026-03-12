print("\n=== TRY / EXCEPT ===")

try:
    x = 10
    y = 2
    print("Result:", x / y)
except Exception as e:
    print("Something went wrong:", e)
