# Autor: Nil Allende Solé       
# Data: 8-10-2025
# Versió: 1
# Descripció: Aquest programa diu si un número a elegir és primer o no
# Especificacions d'entrada: cal donar al programa un número

num = int(input("tria un número positiu "))
contador = 2
while (contador <= num):
    resultat = num % contador
    if resultat != 0:
        contador = contador + 1
        if contador == num:
            print("és primer")
            contador = num +1
    if resultat == 0:
        print("no és primer")
        contador = num + 1
