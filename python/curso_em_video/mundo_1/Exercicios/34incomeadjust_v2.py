# Create a program that applies 15% increase if a salary is less than £1250 and 10% if it is more.

salary = float(input('What is your current salary? £'))

adjusted_salary = salary * 1.15 if salary < 1250 else salary * 1.1

print(f'Your new salary is £{adjusted_salary:.2f}')