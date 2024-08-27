#3) Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input("Digite algo: ")
print("As classe do que você digitou é: ")
print(f"A variável é do tipo {type(algo)}.")
print(f"A variável é do tipo numérico? {algo.isnumeric()}.")
print(f"A variável é do tipo string? {algo.isalpha()}.")
print(f"A variável é do tipo alfanumérico? {algo.isalnum()}")
print(f"A variável é do tipo maiusculo? {algo.isupper()}")
print(f"A variável é do tipo minusculo? {algo.islower()}")

print(f"O que você digitou foi: {algo}.")
