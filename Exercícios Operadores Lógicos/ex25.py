# 25) Um restaurante cobra R$ 25,00 por kg no sistema de comida por peso. Faça um programa que pergunte ao usuário o peso do prato em gramas e calcule o valor a ser pago, considerando que o peso do prato 
# vazio é de 465 gramas.

peso = float(input("Quantos gramas deu o peso do prato? "))

pesototal = (peso-465)/1000
preco = pesototal * 25

print(f"O preco total será de {preco:.2f} reais.")