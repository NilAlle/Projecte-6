# Autor: Nil Allende Solé
# Data: 7/10/2025
# Versió: 1
# Descripció:  Mòdul amb validacions Crea validacions.py amb funcions: es_email_valid(email), es_telefon_valid(telefon)
# Especificacions de entrada: 


import validacions as val

email = str(input("posa un email: "))

telefon = str(input("posa un número de telèfon: "))


if val.es_email_valid(email):
    print("L'email", email, "és vàlid.")
else:
    print("L'email", email, "no és vàlid.")



if val.es_telefon_valid(telefon):
    print("El número de telèfon", telefon, "és vàlid.")
else:
    print("El número de telèfon", telefon, "no és vàlid.")