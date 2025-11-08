# Autor: Nil Allende Solé
# Data: 07/10/2025
# Versió: 1
# Descripció: Escriu una funció multiplica_tot(*nombres) que rebi qualsevol quantitat de nombres i retorni la seva multiplicació
# Especificacions de entrada: ficar el numero de xifres que vols multiplicar i els números que vols multiplicars

num = int(input("Introdueix una quantitat de nombres "))
numeros = [int(input("Introdueix un numero ")) for i in range(num)]


def multiplica_tot(numeros):
    total = 0
    p = 0
    while p < num:
        if p == 0:
            total = numeros[p] * numeros[p + 1]
            p = 2
        total = total * numeros[p]
        p = p + 1
    print(total)
multiplica_tot(numeros)