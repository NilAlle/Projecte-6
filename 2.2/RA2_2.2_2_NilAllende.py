# Autor: Nil Allende Solé       
# Data: 1-10-2025
# Versió: 1
# Descripció: Aquest programa fa un compte atras de 10 segons per despres dir "feliç any nou!"
# Especificacions d'entrada: 

NUMEROS = 101
contador = 0
resultat = 0

while contador < NUMEROS:
    resultat = resultat + contador
    contador = contador + 1

print(resultat)