# Autor: Nil Allende Solé       
# Data: 8-10-2025
# Versió: 1
# Descripció: Aquest programa mostra la succeció de fibonacci
# Especificacions d'entrada: 


a,b = 0,1
contador = 0
while contador < 10:
    print (a)
    suma_termes = a + b
    a = b
    b = suma_termes
    contador = contador + 1