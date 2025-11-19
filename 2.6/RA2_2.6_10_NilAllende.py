# Autor: Nil Allende Solé
# Data: 14/10/2025
# Versió: 1
# Descripció:  Simula una operació amb fitxers on pot haver-hi un error durant la lectura. Assegura’t que el fitxer es tanqui sempre, fins i tot si es produeix un error en llegir-lo.
# Instruccions de entrada: 

f = None
try:
    f = open("missatge.txt", "r")
    contingut = f.read()
    print(contingut)

    # Simulo un error
    a = 10 / 0     

except Exception as e:
    print("S'ha produït un error:", e)

finally:
    if f is not None:
        f.close()
        print("Fitxer tancat.")