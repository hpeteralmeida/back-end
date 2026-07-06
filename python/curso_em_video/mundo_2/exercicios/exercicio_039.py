# Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade < 18:
    print(f"Você ainda vai se alistar. Faltam {18 - idade} anos.")
elif idade == 18:
    print("É a hora de se alistar.")
else:
    print(f"Já passou do tempo de alistamento. Passaram {idade - 18} anos.")