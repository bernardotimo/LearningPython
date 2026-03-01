# Building a dictionary
user = {
    "name": "Bernardo",
    "age": 22,
    "skills": ["Python", "Git", "Java"],
}
print("User:", user)

# Note: "name" is a key and "Bernardo" ia a value associated with the key

# Add / update keys
user["country"] = "Brazil"
user["role"] = "Software Engineer Student"
print("User after updates:", user)

# Build from pairs
pairs = [("a", 1), ("b", 2), ("c", 3)]
d1 = dict(pairs)
print("Dict(pairs):", d1)

#Build with dict comprehension
d2 = {x: x * x for x in range(1, 6)}
print("Square dict:", d2)