# Autor: Nil Allende Solé       
# Data: 8-10-2025
# Versió: 1
# Descripció: Aquest programa elegirà un número aleatori per a que qui l'utilitza l'adivini, quan no l'adivini li dira si el número que ha elegit es superior o inferior al número a adivinar.
# Especificacions d'entrada: Aquest progrrama solicita números de l'u al 100 de manera infinita fins que l'usuari adivini el número que ha pensat el programa

import random
num = random.randint(1,100)
numero = int(input("tria un número entre 1 i 100 "))
if num == numero:
    print("Bravo")
while num != numero:
    if num < numero:
        print("el númor a adivinar és més petit")
        numero = int(input("Posa un altre número "))
    if num > numero:
        print("el númor a adivinar és més gran")
        numero = int(input("Posa un altre número "))
print("Bravo")