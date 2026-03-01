# Strings

word = "Hello,"
name = 'Bernardo'
print(word)
print(name)

# Doesn't work with single quote when the phrase has an apostrophe
# Variable with two names must be written with an underscore
# bakery_name = 'Carl's bakery'#
bakery_name = "Carl's bakery"
print(bakery_name)

# Multi-line string
receipt = """1. Bring a large pot of salted water to boil and cook pasta
2. Heat olive oil in a pan and sauté minced garlic until fragrant
3. Add chopped tomatoes and simmer for 10 minutes
4. Toss cooked pasta with tomato sauce and fresh basil leaves
"""
print(receipt)

# Concatanation, repetition and length
print("Concatenation:", word + " " + name)
print("Repetition:", word * 3)
print("Length:", len(word + " " + name))