# Desenvolva um programa que leia seis 
# numeros inteiros e mostre a soma 
# apenas daqueles que forem pares. Se 
# o valor digitado for impar, 
# desconsidere-o.

soma = 0
pares = 0

for c in range (6):
    numero = int(input(f'Digite o {c+1}º numero: '))

    if numero % 2 == 0:
        soma += numero
        pares += 1

print(f"Ao todo, foram digitados {pares} numeros pares")
print(f"A soma entre eles é: {soma}")
