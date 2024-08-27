#12) Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite seu salário atual: "))
aumento = salario + (salario*15/100)

print(f"Seu salário com 15% de aumento será de {aumento:.2f} reais.")