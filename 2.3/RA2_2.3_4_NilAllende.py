# Autor: Nil Allende Solé       
# Data: 22-10-2025
# Versió: 1
# Descripció: El programa demana a l'usuari un número i diu  tots els números parells fins al número que s'ha triat
# Especificacions d'entrada: demana a l'usuari un número

try:
    num=int(input("posa un número "))

    for i in range(0, num+1, 2):
        print(i)
except ValueError:
    print("has de posar un número enter ")
