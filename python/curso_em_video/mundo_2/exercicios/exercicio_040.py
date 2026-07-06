# `Escreva um programa que leia duas notas de um aluno, calcule e mostre a sua média.
# 

first_grade = float(input("Digite a primeira nota: "))
second_grade = float(input("Digite a segunda nota: "))
mean = (first_grade + second_grade) / 2

if mean < 5:
    print(f"Aluno reprovado! Média: {mean}")
elif 5 <= mean < 7:
    print(f"Recuperacao! Média: {mean}")
else:
    print(f"Aluno aprovado! Média: {mean}")