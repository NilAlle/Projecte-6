# Autor: Nil Allende Solé       
# Data: 8-10-2025
# Versió: 1
# Descripció: Aquest programa imprimira la taula de multiplicar de l'u al deu d'un número elegit
# Especificacions d'entrada: cal donar al programa un número


from time import sleep 
numero = int(input("tria un número "))
for i in [1,2,3,4,5,6,7,8,9,10]:
    sleep(0.25)
    print(i, "·", numero, "=", numero*i)
