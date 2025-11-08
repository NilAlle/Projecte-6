# Autor: Nil Allende Solé
# Data: 07/10/2025
# Versió: 1
# Descripció: Crea un fitxer calculadora.py amb funcions de suma, resta, multiplicació i divisió
# Especificacions de entrada: ficar un numero enter


def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacio(a, b):
    return a * b

def divisio(a, b):
    if b == 0:
        raise ValueError("Divisió per zero no permesa.")
    return a / b
