# Faça um programa que calcule a soma 
# entre todos os números ímpares que são 
# múltiplos de três e que se encontram no 
# intervalo de 1 até 500.


soma = 0
valores = 0

for c in range (1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            valores += 1
            soma += c

print(f'a soma entre os {valores} valores é: {soma}')