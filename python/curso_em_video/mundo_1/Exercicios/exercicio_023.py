# Create a program that reads a number and shows its units, tens, hundreds and thousands

number = int(input('Enter a number between 0 and 9999:'))

print(f'Units: {number // 1 % 10}')
print(f'Tens: {number // 10 % 10}')
print(f'Hundreads: {number // 100 % 10}')
print(f'Thousands: {number // 1000 % 10}')

