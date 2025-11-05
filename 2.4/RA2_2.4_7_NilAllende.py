# Autor: Nil Allende Solé       
# Data: 31-10-2025
# Versió: 1
# Descripció: Conpta les lletres que vol l'usuari que te una paraula o frase
# Especificacions d'entrada: demana a l'usuari una paraula

text = str(input("Introdueix una paraula: "))
lletra = str(input("Introdueix la lletra que vols comptar: "))
contador = text.count(lletra)
print("la lletra", lletra, "apareix", contador, "vegades")