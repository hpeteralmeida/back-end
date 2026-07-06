# Create a program that cheaks if a triagle can exist.

tside_1 = float(input('Enter the triangle side: '))
tside_2 = float(input('Enter the next triangle side: '))
tside_3 = float(input('Enter the last triangle side: '))
if tside_1 + tside_2 > tside_3 and tside_2 + tside_3 > tside_1 and tside_1 + tside_3 > tside_2:
    print('\nThis triangle exists')
else:
    print('\nThis triangle does not exist')