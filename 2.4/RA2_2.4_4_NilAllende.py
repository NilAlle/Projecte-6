# Autor: Nil Allende Solé       
# Data: 31-10-2025
# Versió: 1
# Descripció: Demana una paraula i verifica si és un palíndrom (ex: "anna", "civic", etc.).
# Especificacions d'entrada: demana a l'usuari una paraula

text = str(input("Introdueix una paraula: "))
palindrom = text[::-1]

if palindrom != text:
    print (text, " no és un palindrom")
else:
    print(text, " és un palindrom")