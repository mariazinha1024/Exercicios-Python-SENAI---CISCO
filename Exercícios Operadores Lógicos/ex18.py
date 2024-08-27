# 18) Faça um programa que calcule o IMC(Índice de Massa Corporal) e mostre o resultado na tela. A fórmula é: peso/altura².

peso = float(input("Qual seu peso? "))
altura = (float(input("Qual sua altura em metros? ")))

imc = peso/(altura**2)

print(f"Seu IMC é de: {imc:.2f}")