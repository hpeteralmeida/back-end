# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


loan = float(input("Insira o valor do empréstimo: R$"))
year = int(input("Quantos anos para quitar: "))
salary = float(input("Insira seu salario: R$"))

if loan / (year*12) > salary*0.3:
    print("Empréstimo negado!")
else:
    print(f'Emprestimo aprovado! Valor da parcela: R${loan/(year*12)}')