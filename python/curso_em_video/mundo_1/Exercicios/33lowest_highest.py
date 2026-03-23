# Create a code that reads three values and shows both the lowest and the highest values

first_value = int(input('Type the first value: '))
lowest = first_value
highest = first_value

second_value = int(input('Type the second value: '))
if second_value < lowest:
    lowest = second_value  
else:
    highest = second_value

third_value = int(input('Type the third value: '))
if third_value < lowest:
    lowest = third_value
if third_value > highest:
    highest = third_value

print(f'Lowest value: {lowest}')
print(f'Highest value: {highest}')
