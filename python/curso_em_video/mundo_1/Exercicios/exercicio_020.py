# Create a program that reorder a list of students randomly.

from random import shuffle
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
name3 = input("Enter the third name: ")
name4 = input("Enter the fourth name: ")
names = [name1, name2, name3, name4] # creating a list with the names
#shuffle(names) # the method shuffle() randomly reorder the elements of a list
print(f'The order of the students is {shuffle(names)}')