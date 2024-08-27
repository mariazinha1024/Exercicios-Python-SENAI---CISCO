# 23) Crie um programa que calcule a média ponderada de três notas, considerando os pesos 2, 3 e 5 respectivamente.

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
media = (n1*2+n2*3+n3*5)/(2+3+5)
print(f"A média ponderada total foi de: {media:.2f}")