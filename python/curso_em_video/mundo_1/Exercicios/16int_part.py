# From here, we'll start using libraries
# Create a program that reads a real number and shows only its integer part

from math import trunc # importing the trunc function from the math library
num = float(input("Enter a real number: ")) 
print(f"The integer part of {num} is {trunc(num)}") # the method trunc() returns the integer part of a real number