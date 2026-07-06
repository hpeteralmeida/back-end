# Create a program that shows the sine, cosine and tangent of an angle.

from math import radians, sin, cos, tan
angle = float(input("Enter an angle: "))

print(f'The sine of {angle} is {sin(radians(angle)):.2f}')
print(f'The cosine of {angle} is {cos(radians(angle)):.2f}')
print(f'The tangent of {angle} is {tan(radians(angle)):.2f}')