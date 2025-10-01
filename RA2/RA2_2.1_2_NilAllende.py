# Autor: Nil Allende Solé       
# Data: 1-10-2025
# Descripció: Aquest programa et demana que introdueixis un número per a retornar-te si el número és parell o senar
# Especificacions d'entrada: Aquest programa demana al usuari un número   

num = int(input("tria un número "))
num = num%2
if num == 0:
    print("és parell")
elif num != 0:
    print("és senar")