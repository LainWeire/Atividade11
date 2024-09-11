# Crie um programa que receba a idade de uma pessoa e classifique-a de acordo com as seguintes faixas etárias:
# Criança (0-12 anos)
# Adolescente (13-17 anos)
# Adulto (18-59 anos)
# Idoso (60 anos ou mais)

Id = int(input("Idade: "))
if (Id <= 12):
    print ("Criança")

if (Id <= 17) and (Id >= 13):
    print ("Adolescente")
 
if (Id >= 18) and (Id <= 59):
    print ("Adulto")

if (Id >= 60):
    print ("Idoso")