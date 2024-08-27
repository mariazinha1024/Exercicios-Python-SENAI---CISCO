#7) Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = float(input("Digite um valor em metros: "))
cent = metro*100
mili = cent * 100

print(f"{metro}m convertido em centimetros fica {cent:.2f}cm, já em milimetros fica {mili:.2f}mm.")