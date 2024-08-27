#9) Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere o dólar = R$ 5.49.

real = float(input("Quantos reais você tem na carteira?"))
dolar = real/5.49
print(f"Você pode comprar {dolar:.2f} dólares.")