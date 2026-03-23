# Analisa uma variavel e mostra o seu tipo e verificacoes como se é numero, alfabetoico, alfanumerico, etc

variavel = input("Digite algo: ")
print(f"Voce escreveu algo do tipo {type(variavel)}")
# Nesse primeiro momento, todas as entradas serão consideradas com string
# Com condicionais, podemos verificar e conventer os tipos primitivos
print(f"É um número? {variavel.isnumeric()}")
print(f"É alfabético? {variavel.isalpha()}")
print(f"É alfanumérico? {variavel.isalnum()}")
print(f"Está em maiúsculas? {variavel.isupper()}")
print(f"Está em minúsculas? {variavel.islower()}")