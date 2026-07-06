'''
Create a program that reads the salary of an
employee and shows its new salary with a 15% increase.
'''

salary = float(input("What is the current salary? R$"))
adjusted_salary = salary * 1.15
print(f"The adjusted salary with a 15% increase is R${adjusted_salary:.2f}")