# Autor: Nil Allende Solé       
# Data: 1-10-2025
# Descripció: Aquest programa et demana que introdueixis una lletra per a retornar-te si es consonant o vocal
# Especificacions d'entrada: Aquest programa demana al usuari una lletra

lletra =  str(input("tria una lletra de l'abecedari "))
if lletra == "a" or lletra == "e" or lletra == "i" or lletra == "o" or lletra == "u":
    print("és una vocal")
else:
    print("és una consonant")