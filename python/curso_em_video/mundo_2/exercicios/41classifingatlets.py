# Escreva um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date

birth_year = int(input("Year of birth: "))
actual_year = date.today().year()

age = actual_year - birth_year

if age <= 9:
    print(f'O atleta tem {age} anos\nMIRIM')
elif age <= 14:
    print(f'O atleta tem {age} anos\nINFANTIL')
elif age <= 19:
    print(f'O atleta tem {age} anos\nJUNIOR')
elif age <= 25:
    print(f'O atleta tem {age} anos\nSENIOR')
else:
    print(f'O atleta tem {age} anos\nMASTER')