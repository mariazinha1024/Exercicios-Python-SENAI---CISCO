#15) Faça um programa que calcule o valor total de uma compra. O usuário deve informar o preço de 3 produtos e a quantidade comprada de cada um. Imprima na tela o resultado.

p1 = float(input("Digite o valor do primeiro produto comprado: "))
q1 = int(input("Digite a quantidade do primeiro produto comprado: "))
p2 = float(input("Digite o valor do segundo produto comprado: "))
q2 = int(input("Digite a quantidade do segundo produto comprado: "))
p3 = float(input("Digite o valor do terceiro produto comprado: "))
q3 = int(input("Digite a quantidade do terceiro produto comprado: "))

total = (p1*q1) + (p2*q2) + (p3*q3)

print(f"O total da compra foi de: {total:.2f} reais.")