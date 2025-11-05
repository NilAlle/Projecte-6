# Autor: Nil Allende Solé       
# Data: 5-11-2025
# Versió: 1
# Descripció: Escriu una funció que retorni la llista al revés (sense reverse()).
# Especificacions d'entrada: demana a l'usuari 5 paraules

paraula = [str(input("posa una paraula: ")) for i in range(5)]

llista = list(paraula[::-1])

print(llista)