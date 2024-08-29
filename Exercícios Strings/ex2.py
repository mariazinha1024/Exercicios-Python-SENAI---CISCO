#2) Crie um programa que leia o nome completo de uma pessoas e mostre:
#- O nome com todas as letras maiúsculas;
nome = input('Digite seu nome: ')
print(nome.upper())

#- O nome com todas as letras minúsculas;
nome = input('Digite seu nome: ')
print(nome.lower())

#- Quantas letras ao todo (sem considerar espaços);
s = input('Digite seu nome: ')
print(len(s.replace(" ", "")))

#- Qual o primeiro nome;
nome = input('Digite seu nome: ')
print(nome.split(" ")[0])

#- Quantas letras tem o primeiro nome.
nome = input('Digite seu nome: ')
print(len((nome.split(" ")[0])))