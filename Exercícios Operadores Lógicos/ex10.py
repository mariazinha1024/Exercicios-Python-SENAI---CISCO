# 10) Uma fábrica de refrigerantes produz garrafas de 350ml, 600ml e 2 litros. Crie um programa que peça ao usuário a quantidade produzida de cada tamanho e calcule o volume total de refrigerante produzido em litros.

pequena = int(input("Quantas garrafas de 350ml foram produzidas?"))
media = int(input("Quantas garrafas de 600ml foram produzidas?"))
grande = int(input("Quantas garrafas de 2l foram produzidas?"))

qntpqn = (pequena*350)/1000
qntmedia = (media*600)/1000
qntgrande = grande*2

total = qntpqn+qntgrande+qntmedia

print(f"O volume total produzido foi de: {total} litros.")
