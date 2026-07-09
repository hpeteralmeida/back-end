# Crie um programa que leia
# uma frase qualquer e diga
# se ela é um palíndromo, 
# desconsiderando os espaços.

frase = input("Digite uma frase: ").strip().upper()
palavras = "".join(frase.split())

inverso = palavras[::-1]

print(f'O inverso de {palavras} é {inverso}')
if palavras == inverso:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
