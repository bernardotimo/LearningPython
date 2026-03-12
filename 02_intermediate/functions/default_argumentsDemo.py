# Has a predefined value in the function definition
# If no value is passed, python uses the default value

def greet(name="Guest"):
    print("Hello,", name)
greet("James")
greet()