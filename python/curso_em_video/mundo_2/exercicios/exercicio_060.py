''' Faça um programa que leia um número qualquer e mostre o seu fatorial. '''

num = int(input("Insira um numero para ver o seu fatorial: "))
resultado = 1

while num > 0:
    print(f'{num}', end=' x ' if num > 1 else ' = ')
    resultado *= num
    num -= 1 

print(resultado)