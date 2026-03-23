# Create a program that shows the first and last name of a person.

name = input('What is your name? ').title().strip().split()
print(f'Your first name is {name[0]}')
print(f'Your last name is {name[len(name) - 1]}')