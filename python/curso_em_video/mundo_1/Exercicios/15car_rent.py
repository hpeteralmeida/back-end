'''
Create a program that calculates the price for renting a car
based on how many days and kilmeters the car was used.
Consider that the price per day is R$60.00 and the price per kilometer is R$0.15.
'''

days = int(input("How many days did you rent the car? "))
kilometers = float(input("How many kilometers did you drive? "))

rent_price = (days * 60) + (kilometers * 0.15)
print(f"For {days} days and {kilometers:.2f} kilometers, you'll pay R${rent_price:.2f}")
