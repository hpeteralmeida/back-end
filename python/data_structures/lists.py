# exercício para criar um algoritmo onde um elemento seja inserido sempre no meio da lista


def middle_insert(num):
    meio = len(lista) // 2
    lista.insert(meio, num) 

def first_insert(num):
    lista.insert(0, num)

lista = []

while True:
    if len(lista) == 0:
        print('='*20)
        lista.append(input("Insira o primeiro elemento na lista: \n"))

    else:
        print("="*20)
        print("Escolha uma opcao:")
        print("1 Inserir item no inicio")
        print("2 Inserir item no meio")
        print("3 Inserir item no final")
        print("4 Ver lista")
        print("5 Sair")
        print("="*20)
        opcao = int(input("Digite a opcao: "))

        match opcao:
            case 1:
                num = int(input("Digite o numero a ser inserido: "))
                first_insert(num)
            case 2:            
                num = int(input("Digite o numero a ser inserido: "))
                middle_insert(num)
            case 3:
                num = int(input("Digite o numero a ser inserido: "))
                lista.append(num)
            case 4:
                print(lista)
            case 5:
                print("Saindo...")
                break
            case _:
                print("Opcao invalida, tente novamente.")