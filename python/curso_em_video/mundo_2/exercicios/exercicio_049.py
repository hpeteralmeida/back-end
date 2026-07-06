# Refaça o exercicio 009, mostrando a tabuada de um numero
# utilizando o laço for

valor = int(input('Digite um numero para ver sua tabuada: '))
for i in range(1, 11):
    print(f'{valor} x {i:2} = {valor * i:5}')
