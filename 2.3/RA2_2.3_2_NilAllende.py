# Autor: Nil Allende Solé       
# Data: 17-10-2025
# Versió: 1
# Descripció: El programa demana a l'usuari un número i fa una suma des del seu número fins a l'u per mostrar-la en pantalla
# Especificacions d'entrada: demana a l'usuari un número


try: 
    n = int(input("Introdueix un número "))
    for i in range(1, n+1):
        resultat = sum(range(1, n+1))
    print(resultat)
        
except NameError:
    print("has de posar un número positiu")
except ValueError:
    print("has de posar un número positiu")