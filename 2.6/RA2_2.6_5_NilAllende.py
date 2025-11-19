# Autor: Nil Allende Solé
# Data: 14/10/2025
# Versió: 1
# Descripció: Obre un fitxer en mode lectura i escriptura (r+). Mostra el contingut per pantalla i afegeix una línia al final sense esborrar el contingut anterior.
# Instruccions de entrada: 

with open("sortida.txt", "r+") as f:
    print("Contingut actual:")
    print(f.read())

    f.write("\nNova linia ")