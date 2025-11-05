# Autor: Nil Allende Solé       
# Data: 5-11-2025
# Versió: 1
# Descripció: Demana una llista de paraules i crea una nova llista amb només les paraules que comencen per vocal.
# Especificacions d'entrada: demana a l'usuari 5 paraules

paraules = [str(input("posa una paraula: ")) for i in range(5)]

llista = []
for p in paraules:
    if p[0].lower() in "aeiou":
        llista.append(p)

print(llista)