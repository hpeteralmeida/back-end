# Create a program that reads how much money a person has and convert that to dollars.
# Consider US$1.00 = R$3.27

amount = float(input("How much money do you have? R$"))
amountcoverted = amount / 3.27
print(f"your amount R${amount} in dollar is US${amountcoverted:.2f}")