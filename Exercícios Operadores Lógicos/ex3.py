#3) Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input("Digite algo: ")
print("As classe do que você digitou é: ")
print(type(algo))
print(id(algo))
print(f"O que você digitou foi: {algo}.")
