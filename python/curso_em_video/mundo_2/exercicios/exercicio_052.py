# Faca um programa que leia um numero inteiro e diga se ele e ou nao um numero primo.

numero = int(input("Digite um número inteiro: "))
contador = 0

for i in range(1, numero +1):
    if numero % i == 0:
        contador += 1

if contador == 2:
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")
    