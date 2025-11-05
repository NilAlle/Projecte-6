# Autor: Nil Allende Solé       
# Data: 4-11-2025
# Versió: 1
# Descripció: Demana 10 números i crea dues llistes: una amb els parells i una altra amb els senars.
# Especificacions d'entrada: demana a l'usuari 10 números

numeros = [int(input(f"posa un número {i+1}: ")) for i in range(10)]

parells = []
senars = []
for num in numeros:
    if num % 2 == 0:
        parells.append(num)
    else:
        senars.append(num)

print("números: ", numeros)
print("parells: ", parells)
print("senars: ", senars)

