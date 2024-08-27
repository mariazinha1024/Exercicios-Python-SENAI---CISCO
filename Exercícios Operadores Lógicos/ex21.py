# 21) Desenvolva um programa que calcule o desconto de um produto a partir do preço original e do percentual de desconto fornecidos pelo usuário.

preco = float(input("Qual o valor do produto? "))
desconto = float(input("Quantos % de desconto esse produto terá? "))

total = preco - (preco*desconto/100)
print(f"O preço do produto com {desconto:.2f}% de desconto será de {total:.2f} reais.")