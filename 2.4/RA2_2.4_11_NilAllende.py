# Autor: Nil Allende Solé       
# Data: 4-11-2025
# Versió: 1
# Descripció: Crea una llista amb 5 nombres i imprimeix el major i el menor
# Especificacions d'entrada: demana a l'usuari 5 números

numero = [int(input("posa un número ")),
        int(input("posa un número ")),
        int(input("posa un número ")),
        int(input("posa un número ")),
        int(input("posa un número "))]

major = max(numero)
menor = min(numero)

print("el mes gran és", major, "i el més petit", menor, ".")
