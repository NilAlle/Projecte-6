# Autor: Nil Allende Solé       
# Data: 1-10-2025
# Descripció: Aquest programa et demana que introdueixis tres números per a retornar-te quin dels tres és més gran
# Especificacions d'entrada: Aquest programa demana al usuari tres números

num1 = int(input("tria un primer número "))
num2 = int(input("tria un primer número "))
num3 = int(input("tria un primer número "))

if num1 > num2 and num1 > num3:
    print("el número més gran és el primer")
elif num2 > num1 and num2 > num3:
    print("el número més gran és el segon")
else:
    print("el número més gran és el tercer")