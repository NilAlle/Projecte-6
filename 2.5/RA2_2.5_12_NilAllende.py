# Autor: Nil Allende Solé
# Data: 07/10/2025
# Versió: 1
# Descripció: Crea un mòdul conversions.py amb funcions:celsius_a_fahrenheit(c),fahrenheit_a_celsius(f)
# Especificacions de entrada: ficar un numero enter

import conversions

temperatura = float(input("posa una temperatura en C "))

resultat = conversions.celsius_a_fahrenheit(temperatura)

print(resultat)



temperatura1 = float(input("Fica una temperatura en F "))

resultat1 = conversions.fahrenheit_a_celsius(temperatura1)

print(resultat1)