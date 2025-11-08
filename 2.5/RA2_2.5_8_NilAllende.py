# Autor: Nil Allende Solé
# Data: 07/10/2025
# Versió: 1
# Descripció: Escriu una funció factorial(n) que calculi el factorial d'un nombre n de forma
# Especificacions de entrada: ficar un numero enter

num = int(input("posa un numero "))

def factorial(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    print("El factorial de", n, "és", resultat)

factorial(num)
