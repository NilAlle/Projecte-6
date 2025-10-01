# Autor: Nil Allende Solé       
# Data: 1-10-2025
# Descripció: Aquest programa et demana que introdueixis un número entre 1 i 10 per a retornar-te aprovat o suspes segons la nota
# Especificacions d'entrada: Aquest programa demana al usuari un número entre 1 i 10

num = int(input("posa un número de l'1 al 10 "))
if num >= 5:
    print("Aprovat")
else:
    print("Suspes")