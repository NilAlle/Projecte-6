# Autor: Nil Allende Solé       
# Data: 5-11-2025
# Versió: 1
# Descripció: Fes un programa que elimini els duplicats d'una llista.
# Especificacions d'entrada: demana a l'usuari 5 numeros

numeros = [int(input("posa un número ")),
        int(input("posa un número ")),
        int(input("posa un número ")),
        int(input("posa un número ")),
        int(input("posa un número "))]

no_duplicats = list(set(numeros))

print(no_duplicats)