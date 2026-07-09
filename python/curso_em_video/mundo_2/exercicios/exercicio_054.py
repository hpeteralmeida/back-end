'''Crie um programa que leia o ano 
de nascimento de sete pessoas. No 
final, mostre quantas pessoas 
ainda não atingiram a maioridade e 
quantas já são maiores.'''

from datetime import date

lista_idades = []
maior = 0
menor = 0

for i in range(7):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {i + 1}ª pessoa: "))
    lista_idades.append(ano_nascimento)  

for ano in lista_idades:
    idade = date.today().year - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print(f"Quantidade de pessoas maiores de idade: {maior}")
print(f"Quantidade de pessoas menores de idade: {menor}")
