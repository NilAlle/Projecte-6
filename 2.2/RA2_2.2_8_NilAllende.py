# Autor: Nil Allende Solé       
# Data: 10-10-2025
# Versió: 1
# Descripció: Aquest programa mostra el número el vocals de la frase o paraula que s'introdueix
# Especificacions d'entrada: una paraula o frase

text = str(input("posa algo "))
vocals = "aeiouAEIOU"
contadorvocals = 0
contador = 0

while contador < len(text):
    if text[contador] in vocals:
        contadorvocals = contadorvocals + 1
    contador = contador + 1

print("aqui hi ha", contadorvocals, "vocals")

