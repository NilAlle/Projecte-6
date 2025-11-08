# Autor: Nil Allende Solé
# Data: 7/10/2025
# Versió: 1
# Descripció:  Mòdul amb validacions Crea validacions.py amb funcions: es_email_valid(email), es_telefon_valid(telefon)
# Especificacions de entrada: 

def es_email_valid(email):
    import re
    patró_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patró_email, email) is not None


def es_telefon_valid(telefon):
    import re
    patró_telefon = r'^\+?\d{9,15}$'
    return re.match(patró_telefon, telefon) is not None