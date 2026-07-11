''' Faça um programa que leia o sexo de uma 
pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação 
novamente até ter um valor correto. '''

sexo = input("Digite o sexo da pessoa (M/F): ").strip().upper()

while sexo not in "MF" or sexo == "":
    sexo = input("Sexo inválido. Digite novamente (M/F): ").strip().upper()

print(f"Sexo registrado: {sexo}")