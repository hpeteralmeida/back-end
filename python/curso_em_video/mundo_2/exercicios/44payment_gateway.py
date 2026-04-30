# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

price = float(input("Digite o preço do produto: R$"))
print("Condição de pagamento:")
print("1 - À vista dinheiro/cheque")
print("2 - À vista cartão")
print("3 - Em até 2x no cartão")
print("4 - 3x ou mais no cartão")
option = int(input("Escolha a opção de pagamento (1-4): "))

if option == 1:
    final_price = price * 0.9
elif option == 2:
    final_price = price * 0.95
elif option == 3:
    final_price = price 
elif option == 4:
    final_price = price * 1.2
else:
    print("Opção inválida!")
    final_price = price 

print(f"O valor a ser pago é: R${final_price:.2f}")