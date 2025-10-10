# Autor: Nil Allende Solé       
# Data: 10-10-2025
# Versió: 1
# Descripció: Aquest programa mostra diu quin dels números de l'usuari és el més gran
# Especificacions d'entrada: demanaa l'usuari diversos números separats per espais

llistes = list(map(int, input("posa números separats per espais ").split()))

max = llistes[0]

for num in llistes:
    if num > max:
        max = num
    
print ("el número més gran és", max)
