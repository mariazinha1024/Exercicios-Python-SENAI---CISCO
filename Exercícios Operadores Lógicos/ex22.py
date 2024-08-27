#22) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos. Calcule o total em segundos.

dias = int(input("Digite o numero de dias: "))
horas = int(input("Digite o numero de horas: "))
minutos = int(input("Digite o numero de minutos: "))
segundos = int(input("Digite o numero de segundos: "))

segdias = dias * 24 * 60 * 60
seghoras = horas * 60 * 60
segmin = minutos * 60
total = segdias + seghoras + segmin + segundos
print(f"O total de tempo foi de {total} segundos.")