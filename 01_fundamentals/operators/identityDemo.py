#Identity operators
print("\n===Identity Operators ===")

obj1 = [1, 2]
obj2 = [1, 2]
obj3 = obj1

print("obj1 == obj2 ->", obj1 == obj2) #same content
print("obj1 is obj2 ->", obj1 is obj2) #same object in memory? usually false
print("obj1 is obj3 ->", obj1 is obj3) #True (obj3 references obj1)