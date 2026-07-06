# Pergunte duas notas ao usuário e mostra a média entre essas notas

primeira_nota = float(input("Insira a sua primeira nota: "))
segunda_nota = float(input("Insira a sua segunda nota: "))
media_notas = (primeira_nota+segunda_nota)/2

print(f"A média das suas notas é {media_notas:.2f}")

# {:.2f} é usado para mostrar o número de casas decimais desejado 