# Block of text describing a function

print("\n===  ACCESS ONLY THE DOCSTRING ===")

print(round.__doc__) # "dunder-doc" attribute


print("\n===  AVERAGE DOCSTRING ===")

def average(values):
    # One line docstring
    """Find the mean in a sequence of values and round to two decimal places"""
    average_values = sum(values) / len(values)
    rounded_average = round(average_values, 2)
    return rounded_average
print(average.__doc__)


print("\n===  UPDATING DOCSTRING ===")

average.__doc__ = "Calculate the average value of a list and round to two decimal places"
print(average.__doc__)