''' Refaça o desafio 051, lendo o primeiro 
termo e a razão de uma PA, mostrando 
os 10 primeiros termos da progressão 
usando a estrutura while. '''

primeiro_termo = int(input("Insira o primeiro termo da PA: "))
razao = int(input("Insira a razão da PA: "))

contador = 0
while contador < 10:
    termo = primeiro_termo + contador * razao
    print(termo, end=" -> ")
    contador += 1
    
print("FIM")