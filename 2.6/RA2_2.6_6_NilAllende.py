# Autor: Nil Allende Solé
# Data: 14/10/2025
# Versió: 1
# Descripció: Fes un programa que intenti llegir un fitxer anomenat dades.txt, però abans comprovi si existeix. Si no existeix, mostra un missatge d’error amigable.
# Instruccions de entrada: 

import os

if os.path.exists("dades.txt"):
    with open("dades.txt", "r") as f:
        print(f.read())
else:
    print("ERROR: dades.txt no existeix.")