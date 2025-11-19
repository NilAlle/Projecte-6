# Autor: Nil Allende Solé
# Data: 14/10/2025
# Versió: 1
# Descripció: Suposa que tens un fitxer nombres.txt que hauria de contenir un nombre enter per línia. Fes un programa que llegeixi cada línia i la transformi en enter. Si alguna línia no és un enter vàlid, captura l’error i mostra un missatge, però continua amb la resta.
# Instruccions de entrada: 

with open("nombres.txt", "r") as f:
    for linia in f:
        try:
            numero = int(linia.strip())
            print("Nombre vàlid:", numero)
        except ValueError:
            print("AVÍS: Aquesta línia no és un enter:", linia.strip())