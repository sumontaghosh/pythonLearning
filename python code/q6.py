# Initial values
x = 5
y = 10
z = 15

print(f"Before rotation: x = {x}, y = {y}, z = {z}")

# Rotate values
temp = x
x = y
y = z
z = temp

print(f"After rotation: x = {x}, y = {y}, z = {z}")
