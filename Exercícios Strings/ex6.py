#6) Faça um programa que leia uma frase pelo teclado e mostre:

#- Quantas vezes aparece a letra "A";
frase = input('Digite uma frase: ')
print(frase.lower().count("a"))

#- Em que posição ela aparece a primeira vez;
frase = input('Digite uma frase: ')
print(frase.lower().find("a"))

#- Em que posição ela aparece a ultima vez.
frase = input('Digite uma frase: ')
print(frase.lower().rfind("a"))