# Autor: Nil Allende Solé
# Data: 14/10/2025
# Versió: 1
# Descripció: Aquest programa llegeix el contingut d'un fitxer de text anomenat "missatge.txt" i el mostra per pantalla.
# Instruccions de entrada: 

fitxer = open("missatge.txt", "r")

contingut = fitxer.read()

fitxer.close()

print(contingut)