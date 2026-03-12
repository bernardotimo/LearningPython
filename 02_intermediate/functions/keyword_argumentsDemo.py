# Provide arguments by assigning values to keywords
# The order does not matter

print("\n=== KEYWORD ARGUMENT  ===")

def describe_person(name, age):
    print(name, "is", age, "years old")
describe_person(name="James", age=35)
describe_person(age=22, name="Bob")


print("\n=== DEFAULT + KEYWORD ===")

def order(item, quantity=1):
    print("Order:", quantity, item)
order("Cofee")
order("Cups of Tea", 2)
order(item="Cakes", quantity=2)


print("\n=== ADDING AN ARGUMENT ===")

distance = [25, 32, 15, 115, 87, 36]
def average(numbers, rounded=False):
    if rounded == True:
        average_value = sum(numbers) / len(numbers)
        rounded_average_value = round(average_value, 2)
        return rounded_average_value
    else:
        average_value = sum(numbers) / len(numbers)
        return average_value
print(average(distance, False))
print(average(distance, True))
print(average(distance))