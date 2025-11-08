# Autor: Nil Allende Solé
# Data: 05/10/2025
# Versió: 1
# Descripció: La funció es_parell(numero) que retorni True si numero és parell i False si no
# Especificacions de entrada: ficar un numero enter

num = int(input("posa un numero "))

def es_parell():
    if num % 2 == 0:
        print ("És parell")
    else:
        print("No és parell")

es_parell()