# Working with dictionaries
inventory = {
    "apple": 10,
    "orange": 20,
    "banana": 30,
}
print("Inventory:", inventory)

# Access (unsafe vs safe)
print("Apple:", inventory["apple"])
print("Bread:", inventory.get("bread", 0))
# .get(key, what returns if key doesn't exist)

# Check existence
print("'donut' in inventory:", "donut" in inventory)

# Iterate keys/values/items
print("\nKeys:")
for k in inventory.keys():
    print("-", k)

print("\nValues:")
for v in inventory.values():
    print("-", v)

print("\nItems:")
for k, v in inventory.items():
    print(f"- {k}: {v}")

# Update / merge
inventory.update({"bread": 5, "orange": 6})
print("\nUpdate:", inventory)

# Remove
removed = inventory.pop("orange")
print("Removed:", removed)
print("After removing:", inventory)

# Nested dictionary
students = {
    "Ana": {"grade": 10, "active": True},
    "Bob": {"grade":10, "active": False},
}
print("Students:", students)
print("Ana grade:", students["Ana"]["grade"])