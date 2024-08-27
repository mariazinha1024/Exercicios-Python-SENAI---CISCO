# 13) Faça um programa que calcule a área de um círculo a partir do raio. Imprima na tela o resultado.

raio = float(input("Digite o raio do circulo: "))
pi = float(input("Qual valor de π você deseja considerar? "))
area = pi*raio**2

print(f"A área é de: {area:.2f}u.")