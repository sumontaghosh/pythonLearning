import math

# Circle
radius = 5
circle_area = math.pi * radius ** 2
circle_perimeter = 2 * math.pi * radius

# Square
side_length = 4
square_area = side_length ** 2
square_perimeter = 4 * side_length

# Rectangle
length = 6
width = 3
rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)

# Display the results
print(f"Circle - Area: {circle_area:.2f}, Perimeter: {circle_perimeter:.2f}")
print(f"Square - Area: {square_area}, Perimeter: {square_perimeter}")
print(f"Rectangle - Area: {rectangle_area}, Perimeter: {rectangle_perimeter}")
