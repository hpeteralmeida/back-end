# Create a program that reads the distance of a trip and calculates its price.
# £0.50/km if it's under 200km
# £0.45/km if it's over 200km

distance = int(input('How many kilometres have you driven? '))
price = distance * 0.45 if distance > 200 else distance * 0.5
print(f'The price is £{price:.2f}')