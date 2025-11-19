# Autor: Nil Allende Solé
# Data: 14/10/2025
# Versió: 1
# Descripció: Comptar les linies d'un fitxer 
# Instruccions de entrada: 

with open("sortida.txt", "r") as f:
    linies = f.readlines()
    print("Hi ha", len(linies), "línies.")