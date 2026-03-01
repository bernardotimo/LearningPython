# Choosing a data structure (practical guide)

# LIST: ordered, allows duplicates, easy indexing
tasks = ["study", "code", "sleep"]
tasks.append("repeat")
print("LIST tasks:", tasks)

# TUPLE: ordered, immutable, good for fixed records
rgb = (255, 0, 0)
print("TUPLE rgb:", rgb)

# SET: unordered unique items, fast membership checks
seen_users = {"ana", "leo"}
print("SET seen_users:", seen_users)
print("'ana' seen?:", "ana" in seen_users)

# DICT: key -> value mapping, best for lookup by key
prices = {"bread": 3.5, "donut": 2.0}
print("DICT prices:", prices)
print("price of bread:", prices["bread"])

print("\nRule of thumb:")
print("- Use LIST when you need order + duplicates + indexing")
print("- Use TUPLE for fixed-size records (immutable)")
print("- Use SET for uniqueness and fast 'in' checks")
print("- Use DICT for structured data and fast key lookups")