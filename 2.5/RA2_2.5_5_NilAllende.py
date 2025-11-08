# Autor: Nil Allende Solé
# Data: 05/10/2025
# Versió: 1
# Descripció: La funció saluda_nom(nom="amic") que imprimeixi "Hola, <nom>"
# Especificacions de entrada: ficar una cadena de caracters

nom = str(input("posa el teu nom "))

def saluda_nom():
    if len(nom) == 0:
        print("Hola, amic ")
    else:
        print ("Hola", {nom})

saluda_nom()