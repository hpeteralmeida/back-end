# Create a program that randomly picks a name from a list.

from random import choice 
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
name3 = input("Enter the third name: ")
name4 = input("Enter the fourth name: ")

name = [name1, name2, name3, name4] # creating a list with the names
print(f'The chosen name was {choice(name)}') # the method choice() randomly picks an element from a list