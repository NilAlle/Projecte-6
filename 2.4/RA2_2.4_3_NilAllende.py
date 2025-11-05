# Autor: Nil Allende Solé       
# Data: 31-10-2025
# Versió: 1
# Descripció: Escriu una funció que reverteixi una cadena.
# Especificacions d'entrada: demana a l'usuari un número

text = str(input("Introdueix una línnia de caràcters "))
contador = len(text)
reves = contador - 1


while reves >= 0:
    print(text[reves], end='')
    reves -= 1
