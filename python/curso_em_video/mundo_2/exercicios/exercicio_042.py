# Escreva um programa que leia os comprimentos dos três lados de um triângulo 
# e diga se eles formam um triângulo equilátero, isósceles ou escaleno.

sideA = float(input("Digite o valor do lado A: "))
sideB = float(input("Digite o valor do lado B: "))
sideC = float(input("Digite o valor do lado C: "))

if sideA == sideB == sideC:
    print("Triangulo Equilatero")
elif sideA == sideB != sideC or sideA == sideC != sideB or sideB == sideC != sideA:
    print("Triangulo Isosceles")
else:
    print("Triangulo Escaleno")