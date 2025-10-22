# Autor: Nil Allende Solé       
# Data: 17-10-2025
# Versió: 1
# Descripció: El programa demana a l'usuari un número i fa una llista de la taula de multiplicar d'aquest
# Especificacions d'entrada: demana a l'usuari un número



from time import sleep
try:
    n = int(input("Introdueix un número "))
    for i in range(1, 11):
        resultat = (n*i)
        sleep(0.25)
        print(n, "·", i, "=", resultat)
except ValueError:
    print("has de posar un número enter")