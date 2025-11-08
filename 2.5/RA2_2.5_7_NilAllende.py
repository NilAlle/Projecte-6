# Autor: Nil Allende Solé
# Data: 07/10/2025
# Versió: 1
# Descripció: Escriu una funció maxim(a, b, c) que retorni el nombre més gran entre els tres
# Especificacions de entrada: ficar 3 numeros

a = int(input("Introdueix un numero "))
b = int(input("Introdueix un numero "))
c = int(input("Introdueix un numero "))

def maxim(a, b, c):
    print (max(a, b, c))

maxim(a, b, c)