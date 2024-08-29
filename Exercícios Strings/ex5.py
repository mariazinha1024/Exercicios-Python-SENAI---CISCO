#5) Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
nome = input('Digite o nome da pessoa: ')
verify = nome.lower().find("silva") != -1
print(verify)