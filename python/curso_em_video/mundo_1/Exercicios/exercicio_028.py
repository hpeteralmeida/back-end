# Create a guessing game.

import random

number = random.randint(0, 5)
print('=-' * 20, '=')
guess = int(input("Guess a number between 0 and 5: "))

print(f'You got it right! The number was {number}' if guess == number else f'Wrong! The number was {number}')
