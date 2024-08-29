#exemplo de input
nome = input("Digite o seu nome: ")
idade = input("Informe sua idade: ")
#conteúdo da variável
print("O nome é:", nome)
print("Ela tem", idade, "anos.")
print(f"Ele tem {idade} anos.")
print(type(nome))
print(type(idade)) #sempre que usa input, será string, porém tem que colocar o int dps pra transformar como numero