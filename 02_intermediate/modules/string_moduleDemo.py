# Simplifies text processing tasks
import string
print("\n=== STRINGS CONSTANTS ===")

print("Lowercase letters:", string.ascii_lowercase)
print("Uppercase letters:", string.ascii_uppercase)
print("All letters:", string.ascii_letters)
print("Digits:", string.digits)
print("Hex digits:", string.hexdigits)
print("Punctuation:", string.punctuation)
print("Whitespace:", repr(string.whitespace))


print("\n=== CHECKING CHARACTERS ===")

text = "Hello123!"
letters = [c for c in text if c in string.ascii_letters]
digits = [c for c in text if c in string.digits]
print("Letters:", letters)
print("Digits:", digits)


print("\n=== GENERATING RANDOM PASSWORD ===")

import random
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(10))
print("Random password:", password)

print("\n=== CLEANING TEXT ===")

sentence = "Hey, Mike! How are you? Enjoy it."
clean_text = "".join(c for c in sentence if c not in string.punctuation)
print("Original sentence:", sentence)
print("Cleaned sentence:", clean_text)


print("\n=== STRING TEMPLATE ===")

from string import Template
template = Template("Hello $name, welcome to $place!")
message = template.substitute(name="John", place="London")
print(message)