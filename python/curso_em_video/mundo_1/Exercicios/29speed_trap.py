# Create a code that reads the speed of a car. If it exceeds 80km/h, show a message saying it was fined. The fine is £7.00 for each km above the limit.

speed = int(input('At what velocity was the car moving? '))

if speed > 80:
    fine = (speed - 80) * 7
    print('Speed limit exceeded!')
    print(f'Your fine is £{fine}')
print('Thank you! Drive safe.')