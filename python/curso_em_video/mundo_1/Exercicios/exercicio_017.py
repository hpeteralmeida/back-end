# Create a program thar read the length of the opposite and the adjacent 
# cathetus of a right triangle and calculates the length of the hypotenuse.

from math import hypot 

opposite = float(input("Enter the length of the opposite cathetus: "))
adjacent = float(input("Enter the length of the adjacent cathetus: "))

print(f'the length of the hypotenuse is {hypot(opposite, adjacent):.2f}')