# Create a program that reads a phrase and shows: 
# how many times the letter "a" appears; 
# where it appears first; 
# where it appears last.

phrase = input('Enter a phrase: ').strip().lower()
print(f'The letter "a" appears {phrase.count("a")} times')
print(f'The letter "a" appears first at position {phrase.find("a") + 1}')
print(f'The letter "a" appears last at position {phrase.rfind("a") + 1}')