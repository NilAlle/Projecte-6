# Autor: Nil Allende Solé       
# Data: 31-10-2025
# Versió: 1
# Descripció: Diu la primera i la última lletra de una paraula o frase
# Especificacions d'entrada: demana a l'usuari una paraula

text = str(input("Introdueix una paraula: "))
ultima = len(text) -1
print("la primera lletra és", text[0], "i la última", text[ultima])