# Usage of def statement

print("\n=== FIRST EXAMPLE ===")

nums = [1,2,3,4,5,6,7,8,9,10]

def average(value):
    average_values = sum(value)/len(value)
    rounded_average_values = round(average_values, 2)
    return rounded_average_values
print(average(nums))


print("\n=== FUNCTION USAGE ===")

distance = [24, 86, 335, 84, 12, 56]
print(average(distance))


print("\n===  FUNCTION WITH PARAMETERS ===")

def greet(name):
    print("Hello,", name)

greet("Bernardo")
greet("Milena")



print("\n===  FUNCTION THAT RETURNS A VALUE ===")

def add(a, b):
    result = a + b
    return result
sum_result = add(1, 2)
print(sum_result)



print("\n===  FUNCTION WITH LOGIC ===")

def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print("\n===  DEFAULT PARAMETERS ===")

def create_user(name, role="user"):
    return f"{name} is registered as {role}"

print(create_user("Bernardo"))
print(create_user("Milena","admin"))


print("\n===  PASSWORD VALIDATOR ===")

import string

user_password = input("Please enter your password: ")
def validate_password(password):
    if len(password) >= 8:
        for char in password:
            if char in string.punctuation:
                return True
    return False
is_valid = validate_password(user_password)
print("Is the password valid? ", is_valid)