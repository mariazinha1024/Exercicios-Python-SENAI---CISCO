#26)  Um nutricionista está criando um plano alimentar. Ele precisa calcular o total de calorias e a distribuição de macronutrientes (proteínas, carboidratos e gorduras) de uma refeição. 
# Considerando que 1g de proteína tem 4 calorias, 1g de carboidrato tem 4 calorias e 1g de gordura tem 9 calorias, faça um programa que pergunte a quantidade em gramas de cada macronutriente e calcule o total 
# de calorias e a porcentagem de cada macronutriente em relação ao total de calorias.

pg = int(input("Quantos gramas de proteína tem na refeição? ")) 
cg = int(input("Quantos gramas de carboidratos tem na refeição? ")) 
gg =int(input("Quantos gramas de gordura tem na refeição? "))

totalcp = pg*4
totalcc = cg*4
totalcg = gg*9

totalcal = totalcp + totalcc + totalcg

percprot = totalcal*totalcp/10000
perccarbo = totalcal*totalcc/10000
percgord = totalcal*totalcg/10000

print(f"O total de calorias é de {totalcal} calorias. Há {percprot:.2f}% de proteinas, {perccarbo:.2f}% de carboidratos e {percgord:.2f}% de gordura nessa refeição.")