# Autor: Nil Allende Solé
# Data: 7/10/2025
# Versió: 1
# Descripció: Fes servir el paquet des d’un fitxer principal.
# Especificacions de entrada: 

import temps
import moneda

euro = float(input("posa una quantitat de diners en euros "))
print(moneda.euros_a_dolars(euro))

dolar = float(input("posa una quantitat de diners en dolars "))
print(moneda.dolars_a_euros(dolar))

minuts = int(input("posa una quantitat de temps en minuts "))
print(temps.minuts_a_segons(minuts))