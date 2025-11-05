# Autor: Nil Allende Solé       
# Data: 4-11-2025
# Versió: 1
# Descripció: Crea un programa que divideixi una frase en paraules i les mostri una per una.
# Especificacions d'entrada: demana a l'usuari una paraula

text = str(input("Introdueix una paraula: "))

paraules = text.split()

print("les paraules són")
for paraula in paraules:
    print(paraula)