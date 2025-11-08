# Autor: Nil Allende Solé
# Data: 07/10/2025
# Versió: 1
# Descripció: Escriu una funció estat_persona(edat) que: Retorni "Menor d'edat", "Adult" o "Jubilat" segons l'edat. Torni tant l'estat com una descripció (return estat, descripcio)
# Especificacions de entrada: ficar un numero

edat = int(input("posa la teva edat "))

def estat_persona(edat):
    if edat < 18:
        print("Ets menor d'edat")
    if edat >= 18 and edat < 65:
        print("Ets un adult")
    if edat >= 65:
        print("Estas jubilat")

estat_persona(edat)
