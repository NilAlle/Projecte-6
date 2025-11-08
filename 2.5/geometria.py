# Autor: Nil Allende Solé
# Data: 07/10/2025
# Versió: 1
# Descripció: Escriu un mòdul geometria.py amb funcions:area_quadrat(costat),area_cercle(radi), area_rectangle(base, altura)
# Especificacions de entrada: ficar un numero enter

import math

def area_quadrat(costat):
    return costat ** 2

def area_cercle(radi):
    return math.pi * (radi ** 2)

def area_rectangle(base, altura):
    return base * altura
