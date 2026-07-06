# Create a code that tells if a year is a leap year.
# A leap year is a year that is divisible by 4, but not by 100, except if it is also divisible by 400.

year = int(input('Enter a year, or 0 to check the current year: '))

if year == 0:
    from datetime import date
    year = date.today().year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year} is a leap year')
else: 
    print(f'{year} is not a leap year')