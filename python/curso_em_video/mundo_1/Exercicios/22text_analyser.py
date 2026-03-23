# Crate a program that reads a name and shows its upper and lower forms
# as well as the quantity of letters it has 

name = input('What is your name? ')
 
print(f'Your name in upper letters is {name.upper()}')
print(f'Your name in lower letters is {name.lower()}')
print(f'Your name has {len(name) - name.count(" ")} letters')
first_name = name.split()
print(f'Your first name is {first_name[0].capitalize()} and it has {len(first_name[0])} letters')