# Autor: Nil Allende Solé
# Data: 07/10/2025
# Versió: 1
# Descripció: Crea un fitxer calculadora.py amb funcions de suma, resta, multiplicació i divisió
# Especificacions de entrada: ficar 2 numeros i l'operació

import calculadora

a = int(input("posa un numero "))
b = int(input("posa un numero "))

operacio = input("Quina operació vols fer? ")

if operacio == "+":
    resultat = calculadora.suma(a, b)
    print(resultat)

if operacio == "-":
    resultat = calculadora.resta(a, b)
    print(resultat)

if operacio == "*":
    resultat = calculadora.multiplicacio(a, b)
    print(resultat)
    
if operacio == "/":
    resultat = calculadora.divisio(a, b)
    print(resultat)