# Python scripts that contains reusable code

print("\n=== IMPORTING A MODULE ===")

import math
print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)


print("\n=== IMPORTING SPECIFIC FUNCTIONS ===")
from math import sqrt, pow

print("Square root:", sqrt(25))
print("Power:", pow(2, 3))


print("\n=== USING AN ALIAS ===")

import math as m
print("Cosine of 0:", m.cos(0))


print("\n=== USING BUILT-IN MODULES ===")

import random
print("Random number:", random.randint(1, 10))


print("\n=== USING THE OS MODULE ===")

import os
print("Current working directory:", os.getcwd())


print("\n=== USING THE STRING MODULE ===")

import string
print("Alphabet:", string.ascii_lowercase)
print("Punctuation:", string.punctuation)
