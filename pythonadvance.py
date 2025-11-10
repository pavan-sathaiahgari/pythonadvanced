# Write a function that calculates the below: ( Mathematics - Geometry) 
# Area of the Circle
# Circumference of the Circle
# Volume and Surface area of a Cylinder
# Area of the rectangle
# Perimeter of the rectangle
# Area of the Square

# Write a program to for the below:
# a. The program should take inputs for Five Subjects. English, French, Mathematics, Physics, Chemistry
# b. Maximum Marks is 500 (100 Per Subject)
# c. Calculate the Percentage Scored

# Area of the Circle
radius = float(input('radius ='))
area = 3.14 * radius * radius
print('area of the circle = ', area )
# Circumference of the Circle
circum = 2 * 3.14 * radius
print('circumference = ', circum)

# Volume and Surface area of a Cylinder
height = float(input('height = '))
volume = 3.14 * (radius ** 2) * height
print('volume of cylinder =', volume)

s_area = (2 * 3.14 * radius * height) + (2 * 3.14 * radius * radius)
print('Surface are of cylinder = ', s_area)

# Area & perimeter of the rectangle
length = float(input('length ='))
breadth = float(input('breadth ='))
area = length * breadth
peri = 2 * (length + breadth)

print('area of the rectangle = ', area)
print('perimeter of the rectangle = ', peri)

# Area of the Square
side = float(input('side ='))
area = side ** 2
peri = 4 * side

print('area of the square =', area)
print('perimeter of the square =', peri)

