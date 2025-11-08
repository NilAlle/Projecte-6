# Autor: Nil Allende Solé
# Data: 07/10/2025
# Versió: 1
# Descripció: Escriu una funció filtra_parells(llista) que: Rebi una llista de nombres. Retorni una nova llista només amb els nombres parells
# Especificacions de entrada: ficar 4 numeros

numeros = [int(input("posa un numero ")) for _ in range(4)]

def filtra_parells(llista):
    parells = []
    for n in llista:
        if n % 2 == 0:
            parells.append(n)
    return parells

numeros = filtra_parells(numeros)

print(numeros)