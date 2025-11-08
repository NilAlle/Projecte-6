# Autor: Nil Allende Solé
# Data: 07/10/2025
# Versió: 1
# Descripció: Escriu un mòdul geometria.py amb funcions:area_quadrat(costat),area_cercle(radi), area_rectangle(base, altura)
# Especificacions de entrada: ficar un numero enter

import geometria

costat = int(input("posa el costat del quadrat "))
print("L'Àrea és", geometria.area_quadrat(costat))

radi = int(input("posa el radi del cercle "))
print("L'Àrea és", geometria.area_cercle(radi))

base = int(input("posa la base del rectangle "))
altura = int(input("posa  l'altura del rectangle "))
print("L'Àrea  és", geometria.area_rectangle(base, altura))