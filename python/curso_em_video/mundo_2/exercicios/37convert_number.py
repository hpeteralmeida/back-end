# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input("Digite um numero inteiro: "))
opcao = int(input("Escolha a base de conversão: \n1 Binário\n2 Octal\n3 Hexadecimal\n"))
match opcao:
    case 1:        
        print(f"O numero {numero} em binário é: {bin(numero)[2:]}")      
    case 2:
        print(f"O numero {numero} em octal é: {oct(numero)[2:]}")
    case 3:
        print(f"O numero {numero} em hexadecimal é: {hex(numero)[2:]}")