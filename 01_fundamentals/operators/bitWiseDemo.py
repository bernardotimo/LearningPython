#BitWise Operators
print("\n=== BitWise Operators ===")
p,q = 6, 3 #6 -> 110 (binary), 3 -> 011
print("p = ", p, "(bin: ", bin(p) + ")", "q = ", q, "(bin: ", bin(q) + ")")
print("p & q  ->", p & q,  "(bin:", bin(p & q) + ")")  # AND
print("p | q  ->", p | q,  "(bin:", bin(p | q) + ")")  # OR
print("p ^ q  ->", p ^ q,  "(bin:", bin(p ^ q) + ")")  # XOR
print("~p ->", ~p) # NOT (two's complement)
print("p << 1 ->", p << 1, "(bin:", bin(p << 1) + ")") # left shift
print("p >> 1 ->", p >> 1, "(bin:", bin(p >> 1) + ")") # right shift

#Raw bits
print("\nRaw bits:", bin(p)[2:])

#Internally, python does not store numbers as binary with 0b
x = 0b110
y = 6

print("\nIs x == y:", x == y)