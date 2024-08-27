# 24) Crie um programa que calcule o consumo médio de um carro, pedindo a distância percorrida e o total de combustível gasto.

km = float(input("Quantos quilômetros foram percorridos? "))
litros = float(input("Quantos litros foram consumidos? "))

kml = km/litros
print(f"Seu carro faz {kml:.2f} km/l em média.")