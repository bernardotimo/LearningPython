print("\n=== ELSE BLOCK ===")

try: # code that may fail
    value = int("5")
except ValueError: # runs if an error happens
    print("Invalid input")
else: # runs if no errors happens
    print("The value entered is an integer:", value)



print("\n=== FINALLY BLOCK ===")

try:
    file = open("file.txt", "w")
    file.write("Hello World")
except Exception as e:
    print("Error:", e)
finally: #always runs
    file.close()
    print("File closed")