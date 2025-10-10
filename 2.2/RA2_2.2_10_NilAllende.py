# Autor: Nil Allende Solé       
# Data: 10-10-2025
# Versió: 1
# Descripció: Aquest programa mostra un patró "triangular"
# Especificacions d'entrada:

asterikos ="*"
contador = 0

while contador != 10:
    print(asterikos.center(30))
    asterikos = asterikos + "*"
    contador = contador + 1