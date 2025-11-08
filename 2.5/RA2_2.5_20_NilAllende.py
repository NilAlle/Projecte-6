# Autor: Nil Allende Solé
# Data: 7/10/2025
# Versió: 1
# Descripció:  Mòdul amb validacions Crea validacions.py amb funcions: es_email_valid(email), es_telefon_valid(telefon)
# Especificacions de entrada: 


import cientifica
import math
import calculadora

cientifica.mostrar_menu()
comanda = str(input("posa la comanda: "))

if comanda == "1":
    num1 = float(input("posa el primer número: "))
    num2 = float(input("posa el segon número: "))
    resultat = calculadora.suma(num1, num2)
    print("El resultat de la suma és:", resultat)

if comanda == "2":
    num1 = float(input("posa el primer número: "))
    num2 = float(input("posa el segon número: "))
    resultat = calculadora.resta(num1, num2)
    print("El resultat de la resta és:", resultat)

if comanda == "3":
    num1 = float(input("posa el primer número: "))
    num2 = float(input("posa el segon número: "))
    resultat = calculadora.multiplicacio(num1, num2)
    print("El resultat de la multiplicació és:", resultat)

if comanda == "4":
    num1 = float(input("posa el primer número: "))
    num2 = float(input("posa el segon número: "))
    resultat = calculadora.divisio(num1, num2)
    print("El resultat de la divisió és:", resultat)

if comanda == "5":
    num1 = float(input("posa la base: "))
    num2 = float(input("posa l'exponent: "))
    resultat = cientifica.potencia(num1, num2)
    print("El resultat de la potència és:", resultat)

if comanda == "6":
    num = float(input("posa un número: "))
    resultat = math.sqrt(num)
    print("L'arrel quadrada de", num, "és:", resultat)

if comanda == "7":
    angle = float(input("posa un angle en graus: "))
    resultat = math.sin(math.radians(angle))
    print("El seno de", angle, "graus és:", resultat)

if comanda == "8":
    angle = float(input("posa un angle en graus: "))
    resultat = math.cos(math.radians(angle))
    print("El coseno de", angle, "graus és:", resultat)

if comanda == "9":
    angle = float(input("posa un angle en graus: "))
    resultat = math.tan(math.radians(angle))
    print("La tangent de", angle, "graus és:", resultat)