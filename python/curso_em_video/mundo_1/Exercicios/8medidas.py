# Leia um valor em metros e transforme em centrimetros e milimetros

medida_m = float(input("Insira a medida em metros: "))
medida_cm = medida_m * 100
medida_mm = medida_m * 1000
print(f"A medida {medida_m}m em centímetros é {medida_cm}cm")
print(f"A medida {medida_m}m em milimetros é {medida_mm}mm")