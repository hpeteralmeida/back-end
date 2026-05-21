# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice

jogada_computador = choice(['Pedra', 'Papel', 'Tesoura'])

print('==============================\n' \
'    Pedra Papel Tesoura\n' \
'==============================\n' \
'1. Pedra \n' \
'2. Papel \n' \
'3. Tesoura\n' \
'==============================')
jogada_user = int(input('Sua jogada: '))

if jogada_user == 1:
    jogada_user = 'Pedra'
elif jogada_user == 2:
    jogada_user = 'Papel'
else:
    jogada_user = 'Tesoura'

if jogada_computador == jogada_user:
    print(f'Computador: {jogada_computador}')
    print(f'Jogador: {jogada_user}')
    print('EMPATE!')

elif jogada_computador == 'Pedra' and jogada_user == 'Papel' or jogada_computador == 'Papel' and jogada_user == 'Tesoura' or jogada_computador == 'Tesoura' and jogada_user == 'Pedra':
    print(f'Computador: {jogada_computador}')
    print(f'Jogador: {jogada_user}')
    print('Você GANHOU!')

else:
    print(f'Computador: {jogada_computador}')
    print(f'Jogador: {jogada_user}')
    print('Você PERDEU!')
