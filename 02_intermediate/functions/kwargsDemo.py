#Arbitrary keywords arguments
# Accepts any number of keywords arguments

def show_profile(**details): # details becomes a dictionary
    for key, value in details.items():
        print(key, ":", value)

show_profile(name="Alice", age=25, city="Tokyo")