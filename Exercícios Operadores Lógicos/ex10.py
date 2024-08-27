# 10) Uma fábrica de refrigerantes produz garrafas de 350ml, 600ml e 2 litros. Crie um programa que peça ao usuário a quantidade produzida de cada tamanho e calcule o volume total de refrigerante produzido em litros.

pequena = int(input("Quantos litros foram produzidos para as garradas de 350ml?"))
media = int(input("Quantos litros foram produzidos para as garradas de 600ml?"))
grande = int(input("Quantos litros foram produzidos para as garradas de 2l?"))

total = pequena + media + grande
print(f"o volume total produzido foi de: {total} litros.")