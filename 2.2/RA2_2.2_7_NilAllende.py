# Autor: Nil Allende Solé       
# Data: 9-10-2025
# Versió: 1
# Descripció: Aquest programa mostra el que posi l'usuari al revès
# Especificacions d'entrada: una paraula o frase

text = str(input("posa algo "))
nom = len(text)
contador = nom - 1

while contador >= 0:
    print(text[contador], end="")
    contador = contador - 1