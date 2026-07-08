# Desenvolva um programa que leia o 
# primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros 
# termos dessa progressão.

inicio = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

for i in range(10):
    termo = inicio + i * razao
    print(termo, end=" -> ")
print("FIM")
