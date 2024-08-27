#17) Escreva um programa para determinar se uma pessoa deve ou não pagar imposto. Considere que pagam imposto pessoa cujo salário é maior de R$ 1200,00.

salario = float(input("Digite seu salário: "))
if salario >= 1200:
  print("Você pagará imposto.")
else:
  print("Você não pagará imposto.")