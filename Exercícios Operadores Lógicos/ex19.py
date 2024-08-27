#19) Escreva um programa que converta uma temperatura digitada em Graus Celsius em Graus Fahrenheit. A fórmula para essa conversão é: celsius * 9/5 + 32.

celsius = float(input("Digite a quatidade de Graus Celsius "))

fahrenheit = celsius*9/5+32
print(f"Está fazendo {fahrenheit:.1f}F.")