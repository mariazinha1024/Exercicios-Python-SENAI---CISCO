#11) Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Digite o preco do produto: "))

total = preco - (preco*5/100)
print(f"O preco total com 5% de desconto foi de: {total:.2f} reais.")