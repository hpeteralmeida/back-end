# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

first_number = int(input("Digite o primeiro numero: "))
second_number = int(input("Digite o segundo numero: "))

if first_number > second_number:
    print(f"O primeiro valor é maior: {first_number}")
elif second_number > first_number:
    print(f"O segundo valor é maior: {second_number}")
else:
    print("Não existe valor maior, os dois são iguais.")
