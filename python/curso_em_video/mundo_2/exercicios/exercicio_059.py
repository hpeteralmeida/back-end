''' Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. '''

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

while True:
    print('''Escolha uma das opções abaixo:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    
    opcao = int(input('Digite a opção desejada: '))
    
    if opcao == 1:
        soma = valor1 + valor2
        print(f'A soma entre {valor1} e {valor2} é {soma}.')
        
    elif opcao == 2:
        multiplicacao = valor1 * valor2
        print(f'O resultado da multiplicação entre {valor1} e {valor2} é {multiplicacao}.')
        
    elif opcao == 3:
        if valor1 > valor2:
            print(f'O maior valor entre {valor1} e {valor2} é {valor1}.')
        elif valor2 > valor1:
            print(f'O maior valor entre {valor1} e {valor2} é {valor2}.')
        else:
            print('Os dois valores são iguais.')
            
    elif opcao == 4:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
        
    elif opcao == 5:
        print('Saindo do programa...')
        break
        
    else:
        print('Opção inválida. Tente novamente.')