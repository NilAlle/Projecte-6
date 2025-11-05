# Autor: Nil Allende Solé       
# Data: 31-10-2025
# Versió: 1
# Descripció: Escriu una funció que elimini tots els espais d'una cadena.
# Especificacions d'entrada: demana a l'usuari una paraula

text = str(input("Introdueix una paraula: "))

espais = text.replace(" ", "")

print(espais)