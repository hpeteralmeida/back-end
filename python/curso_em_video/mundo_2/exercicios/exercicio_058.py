''' Melhore o jogo do desafio 028 onde o computador vai 
"pensar" em um número entre 0 e 10. Só que agora o 
jogador vai tentar adivinhar até acertar, mostrando 
no final quantos palpites foram necessários para vencer. '''

from random import randint

computador = randint(0, 10)

print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
palpites = 0

while True:  
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        break
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')

print(f'Acertou! O número que eu pensei foi {computador}.')
print(f'Você precisou de {palpites} palpites para acertar.')