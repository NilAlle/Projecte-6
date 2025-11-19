# Autor: Nil Allende Solé
# Data: 14/10/2025
# Versió: 1
# Descripció: Intenta obrir un fitxer en mode lectura. Si no existeix, crea’l automàticament i escriu-hi una línia per defecte: "Fitxer creat automàticament".
# Instruccions de entrada: 

try:
    with open("prova.txt", "r") as f:
        print("Fitxer existent:")
        print(f.read())
except FileNotFoundError:
    with open("prova.txt", "w") as f:
        f.write("Fitxer creat automaticament\n")
    print("Nou fitxer creat, no existia.")