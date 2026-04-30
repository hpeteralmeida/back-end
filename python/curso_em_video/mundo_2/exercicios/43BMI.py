# Escreva um programa que leia o peso e a altura de uma pessoa, calcule o seu Índice de Massa Corporal (IMC) e mostre o resultado na tela, juntamente com uma mensagem indicando a faixa de peso da pessoa (abaixo do peso, peso ideal, sobrepeso, obesidade).
weight = float(input("Digite o peso (kg): "))
height = float(input("Digite a altura (m): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"Seu IMC é {bmi:.2f}. Você está abaixo do peso.")
elif 18.5 <= bmi < 25:
    print(f"Seu IMC é {bmi:.2f}. Você está com peso ideal.")
elif 25 <= bmi < 30:
    print(f"Seu IMC é {bmi:.2f}. Você está com sobrepeso.")
else:
    print(f"Seu IMC é {bmi:.2f}. Você está obeso.")