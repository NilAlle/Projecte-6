# Autor: Nil Allende Solé
# Data: 14/10/2025
# Versió: 1
# Descripció: Escriu un programa que intenti escriure en un fitxer anomenat resultats.txt, però gestiona l'error que es pot produir si el fitxer és només de lectura o si el sistema impedeix escriure-hi (permisos denegats).
# Instruccions de entrada: 

try:
    with open("resultats.txt", "w") as f:
        f.write("Prova d'escriptura.\n")
except PermissionError:
    print("ERROR: No tens permís per escriure al fitxer resultats.txt.")