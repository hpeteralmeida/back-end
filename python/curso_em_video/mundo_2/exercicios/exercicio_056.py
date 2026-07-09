
soma_idades = 0
homem_mais_velho = ''
idade_homem_mais_velho = 0
mulheres_jovens = 0

for i in range(4):
    print(f'----- {i + 1}ª PESSOA -----')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    
    soma_idades += idade

    if sexo == 'M':
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            homem_mais_velho = nome
    else:
        if idade < 20:
            mulheres_jovens += 1

print(f'A média de idade do grupo é de {soma_idades / 4:.1f} anos.')
print(f'O homem mais velho tem {idade_homem_mais_velho} anos e se chama {homem_mais_velho}.')
print(f'Ao todo são {mulheres_jovens} mulheres com menos de 20 anos.')
   
