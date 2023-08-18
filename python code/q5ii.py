# Without using a third variable for swapping
a = 5
b = 10

print(f"Before swapping: a = {a}, b = {b}")

a = a + b
b = a - b
a = a - b

print(f"After swapping: a = {a}, b = {b}")
