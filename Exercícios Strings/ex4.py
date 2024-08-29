#4) Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

nome = input('Digite o nome da cidade: ')
print("santo" == nome.lower().split(" ")[0])