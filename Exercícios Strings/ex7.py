#7) Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente. Exemplo: Ana Maria De Souza

#- Primeiro: Ana
nome = input('Digite seu nome: ')
print(nome.split(" ")[0])

#- Ultimo: Souza
nome = input('Digite seu nome: ')
print(nome.split(" ")[-1])