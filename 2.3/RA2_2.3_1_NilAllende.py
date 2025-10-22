# Autor: Nil Allende Solé       
# Data: 10-10-2025
# Versió: 1
# Descripció: El programa demana a l'usuari un número i fa una llista des de 0 fins al seu número
# Especificacions d'entrada: demana a l'usuari un número

try:
    n = int(input("Introdueix un número "))
    for i in range(0, n):
        print (i)
except ValueError:
    print("Has d'introdueir un número enter")
