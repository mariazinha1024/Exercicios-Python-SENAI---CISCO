#20) Escreva um programa que receba o salário bruto de um funcionário, bem como os percentuais de descontos de INSS, Imposto de Renda, e um valor de bonificação. O funcionário recebe 30% do valor do salário bruto no dia 
# 15 e o restante em um segundo pagamento no final do mês, dia 30. O programa deve calcular e exibir o salário final do funcionário após aplicar os descontos e a bonificação.

salario = float(input("Qual o seu salário bruto? "))
inss = float(input("Quanto é descontado de INSS do seu salário? "))
ir = float(input("Quanto é descontado de Imposto de Renda do seu salário? "))
bonificacao = float(input("Quanto de bonificação você recebe? "))

total = salario-inss-ir+bonificacao
salario1 = total*30/100
salario2 = total-salario1
print(f"Você receberá {total:.2f} reais, sendo {salario1:.2f} reais no dia 15 e {salario2:.2f} reais no dia 30.")